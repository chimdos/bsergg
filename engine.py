import numpy as np
from typing import List, Dict
from .models import PlayerPerformance
from .constants import (
    BRAWLER_ROSTER, CLASS_BASE_WEIGHTS, CLASS_EXPECTED_OUTPUT,
    EXPECTATION_MATRIX, MODE_BASE_DIVISORS, MAP_ADJUSTMENTS,
    HEIST_BURNERS
)

class BSERRatingEngine:
    """
    Engine v1.1.0: Context-aware performance analysis for Brawl Stars Esports.
    This class handles the core mathematical normalization of professional match data.
    """

    def __init__(self, players: List[PlayerPerformance], mode: str, map_name: str, confrontation: str):
        self.players = players
        self.gamemode = mode
        self.map_name = map_name
        self.confrontation = confrontation
        self._initialize_match_context()

    def _initialize_match_context(self):
        """Pre-calculates match-wide baselines used for normalization across all players."""
        self.map_modifier = MAP_ADJUSTMENTS.get(self.map_name, {"dps": 1.0, "kills": 1.0})
        base_dps_divisor, base_kills_divisor = MODE_BASE_DIVISORS.get(self.gamemode, (250, 7.0))
        
        # Match targets adjusted by map geometry
        self.target_dps = base_dps_divisor * self.map_modifier['dps']
        self.target_kills = base_kills_divisor * self.map_modifier['kills']
        
        # Collective lobby performance
        self.avg_match_dps = np.mean([p.dps for p in self.players])
        self.avg_match_kills = np.mean([p.kills for p in self.players])

    def calculate_all(self) -> List[Dict]:
        """Orchestrates and returns the rating analysis for the entire match lobby."""
        return [self._process_player_stats(index, player) for index, player in enumerate(self.players)]

    def _process_player_stats(self, index: int, player: PlayerPerformance) -> Dict:
        """Translates raw player stats into the BSER standardized output format."""
        brawler_class = BRAWLER_ROSTER.get(player.brawler, ["Hybrid"])[0]
        
        # Core Skill Metric calculation
        technical_score = self._compute_technical_score(player, brawler_class)
        
        # Final Rating logic (Heist vs Standard)
        if self.gamemode == "Heist":
            final_rating = self._apply_heist_scoring(player, technical_score, brawler_class)
        else:
            final_rating = self._apply_standard_scoring(player, technical_score, brawler_class)

        return {
            "name": player.name,
            "brawler": player.brawler,
            "rating": round(max(0.15, final_rating), 2),
            "ksh": round(self._calculate_kill_share(player, index), 1),
            "dvs_e": round(self._calculate_damage_vs_expected(player, brawler_class), 1)
        }

    def _calculate_kill_share(self, player: PlayerPerformance, player_index: int) -> float:
        """Computes the percentage of team kills performed by this player."""
        team_players = self.players[:3] if player_index < 3 else self.players[3:]
        total_team_kills = sum(p.kills for p in team_players)
        
        if total_team_kills == 0:
            return 33.3
        return (player.kills / total_team_kills) * 100

    def _calculate_damage_vs_expected(self, player: PlayerPerformance, brawler_class: str) -> float:
        """Calculates DvsE% by cross-referencing class output, mode attenuators, and match pace."""
        output_factor = CLASS_EXPECTED_OUTPUT.get(brawler_class, 1.15)
        gamemode_attenuator = EXPECTATION_MATRIX.get(self.gamemode, {}).get(brawler_class, 1.0)
        
        # Match Pace Mod: prevents rating inflation/deflation based on lobby activity
        match_pace_modifier = max(0.7, min(1.3, self.avg_match_dps / self.target_dps))
        
        expected_dps = (self.target_dps * (output_factor / 1.15)) * gamemode_attenuator * match_pace_modifier
        return ((player.dps / expected_dps) - 1) * 100

    def _compute_technical_score(self, player: PlayerPerformance, brawler_class: str) -> float:
        """Computes the skill score using weights from CLASS_BASE_WEIGHTS"""
        weights = CLASS_BASE_WEIGHTS.get(brawler_class, CLASS_BASE_WEIGHTS["Hybrid"])
        
        # Comparison baseline (60% Lobby Average / 40% Global Target)
        comparison_kills = (self.avg_match_kills * 0.6) + (self.target_kills * 0.4)
        comparison_dps = (self.avg_match_dps * 0.6) + (self.target_dps * 0.4)
        
        # Elastic normalization
        kill_skill_score = pow((player.kills + 2.5) / (comparison_kills + 2.5), 0.75)
        damage_skill_score = pow((player.dps + 120) / (comparison_dps + 120), 0.75)
        
        # Dynamic weighting based on Brawler Class
        total_weight = weights['kills'] + weights['dps']
        return (kill_skill_score * weights['kills'] + damage_skill_score * weights['dps']) / total_weight

    def _apply_heist_scoring(self, player: PlayerPerformance, tech_score: float, brawler_class: str) -> float:
        """Applies Heist-specific logic using HEIST_BURNERS"""
        is_match_long = any(s in self.confrontation for s in ["2-1", "1-2"])
        safe_hp = 80000 * (3 if is_match_long else 2)
        
        # Safe damage normalization
        average_dts = np.mean([p.damage_to_safe for p in self.players])
        relative_dts = player.damage_to_safe / average_dts if average_dts > 0 else 1.0
        absolute_dts = player.damage_to_safe / (safe_hp * 0.3)
        dts_score = (relative_dts * 0.4) + (absolute_dts * 0.6)
        
        # Burners focus 70% on Safe Damage, others 30%
        if player.brawler in HEIST_BURNERS:
            score = (tech_score * 0.3) + (dts_score * 0.7)
        else:
            score = (tech_score * 0.7) + (dts_score * 0.3)
            
        return self._finalize_rating(player, score, brawler_class)

    def _apply_standard_scoring(self, player: PlayerPerformance, tech_score: float, brawler_class: str) -> float:
        """Finalizes score for non-Heist game modes."""
        return self._finalize_rating(player, tech_score, brawler_class)

    def _finalize_rating(self, player: PlayerPerformance, score: float, brawler_class: str) -> float:
        """Applies win bonuses, situational buffs, and standard multipliers."""
        if player.won:
            score += 0.15 # Additive win contribution
        
        # Contextual multipliers
        win_modifier = 1.10 if player.won else 0.96
        brawler_modifier = 1.25 if player.brawler == "Doug" else (1.15 if player.brawler == "Poco" else 1.0)
        mode_modifier = 1.15 if (self.gamemode == "Brawl Ball" and brawler_class == "Tank") else 1.0
        
        return score * win_modifier * brawler_modifier * mode_modifier