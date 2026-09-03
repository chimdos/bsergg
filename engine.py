import math
import logging
from abc import ABC, abstractmethod
from typing import List, Dict, Any

from .models import PlayerPerformance, MatchContext
from .constants import (
    BRAWLERS_DATABASE,
    CLASS_PERFORMANCE_WEIGHTS,
    CLASS_DPS_OUTPUT,
    EXPECTATION_MATRIX,
    HEIST_BURNERS,
    HEIST_SAFE_MAX_HP,
    HEIST_OBJECTIVE_BENCHMARK_RATIO,
    HEIST_OBJECTIVE_CAP,
    ELASTIC_POWER_CURVE,
    KILL_ELASTIC_OFFSET,
    DAMAGE_ELASTIC_OFFSET
)

logger = logging.getLogger(__name__)


class MatchBaseline:
    """Pre-calculates static mathematical averages for a specific lobby."""
    
    def __init__(self, players: List[PlayerPerformance]):
        self._players = players
        self.mean_damage = self._calculate_lobby_mean_damage()
        self.mean_kills = self._calculate_lobby_mean_kills()

    def _calculate_lobby_mean_damage(self) -> float:
        if not self._players:
            return 100.0
        total_damage = sum(player.average_damage for player in self._players)
        return max(100.0, total_damage / len(self._players))

    def _calculate_lobby_mean_kills(self) -> float:
        if not self._players:
            return 1.0
        total_kills = sum(player.average_kills for player in self._players)
        return max(1.0, total_kills / len(self._players))

    def retrieve_team_kills(self, is_team_one: bool) -> float:
        team_roster = self._players[:3] if is_team_one else self._players[3:]
        return sum(player.average_kills for player in team_roster)


class MechanicalSkillEvaluator:
    """Computes the core mechanical score based on curve-adjusted outputs."""
    
    def __init__(self, baseline: MatchBaseline, current_mode: str):
        self._baseline = baseline
        self._current_mode = current_mode

    def evaluate(self, player: PlayerPerformance, brawler_class: str) -> float:
        performance_weights = CLASS_PERFORMANCE_WEIGHTS.get(brawler_class, {"kills": 1.0, "dps": 1.0})
        
        kills_score = self._calculate_kills_score(player.average_kills, performance_weights["kills"])
        damage_score = self._calculate_damage_score(player.average_damage, brawler_class)

        total_weight = performance_weights["kills"] + performance_weights["dps"]
        weighted_kills = kills_score * performance_weights["kills"]
        weighted_damage = damage_score * performance_weights["dps"]
        
        return (weighted_kills + weighted_damage) / total_weight

    def get_expected_damage(self, brawler_class: str) -> float:
        output_multiplier = CLASS_DPS_OUTPUT.get(brawler_class, 1.15)
        mode_modifier = EXPECTATION_MATRIX.get(self._current_mode, {}).get(brawler_class, 1.0)
        return self._baseline.mean_damage * (output_multiplier / 1.15) * mode_modifier

    def _calculate_damage_score(self, actual_damage: float, brawler_class: str) -> float:
        expected_damage = self.get_expected_damage(brawler_class)
        return self._apply_elastic_curve(actual_damage, expected_damage, DAMAGE_ELASTIC_OFFSET)

    def _calculate_kills_score(self, actual_kills: float, kill_weight: float) -> float:
        expected_kills = self._baseline.mean_kills * (kill_weight / 1.05)
        return self._apply_elastic_curve(actual_kills, expected_kills, KILL_ELASTIC_OFFSET)

    def _apply_elastic_curve(self, achieved: float, expected: float, variance_offset: float) -> float:
        performance_ratio = (achieved + variance_offset) / (expected + variance_offset)
        return math.pow(performance_ratio, ELASTIC_POWER_CURVE)


class IRatingStrategy(ABC):
    """Dependency Inversion for mode-specific tactical scoring."""
    
    @abstractmethod
    def evaluate(self, player: PlayerPerformance, mechanical_score: float) -> float:
        pass


class StandardStrategy(IRatingStrategy):
    def evaluate(self, player: PlayerPerformance, mechanical_score: float) -> float:
        return mechanical_score


class HeistStrategy(IRatingStrategy):
    def evaluate(self, player: PlayerPerformance, mechanical_score: float) -> float:
        objective_ratio = self._calculate_objective_ratio(player.average_damage_to_safe)
        
        if player.brawler in HEIST_BURNERS:
            return self._calculate_burner_score(mechanical_score, objective_ratio)
            
        return self._calculate_defender_score(mechanical_score, objective_ratio)

    def _calculate_objective_ratio(self, damage_to_safe: float) -> float:
        target_benchmark = HEIST_SAFE_MAX_HP * HEIST_OBJECTIVE_BENCHMARK_RATIO
        raw_ratio = damage_to_safe / target_benchmark
        return min(raw_ratio, HEIST_OBJECTIVE_CAP)

    def _calculate_burner_score(self, mechanical_score: float, objective_ratio: float) -> float:
        return (mechanical_score * 0.60) + (objective_ratio * 0.40)

    def _calculate_defender_score(self, mechanical_score: float, objective_ratio: float) -> float:
        return mechanical_score * (0.90 + (objective_ratio * 0.10))


class BSERRatingEngine:
    """Orchestrates dependencies to generate final match reports."""
    
    def __init__(self, context: MatchContext):
        self._context = context
        self._normalized_mode = context.resolve_normalized_mode()
        self._baseline = MatchBaseline(context.players)
        self._skill_evaluator = MechanicalSkillEvaluator(self._baseline, self._normalized_mode)
        self._tactical_strategy = self._inject_tactical_strategy()

    def _inject_tactical_strategy(self) -> IRatingStrategy:
        if self._normalized_mode == "Heist":
            return HeistStrategy()
        return y()

    def process_match_ratings(self) -> List[Dict[str, Any]]:
        try:
            if not self._context.players:
                raise ValueError("MatchContext contains no player data. Cannot compute ratings.")
                
            return [self._evaluate_individual(player, idx) for idx, player in enumerate(self._context.players)]
        except Exception as error:
            logger.error(f"Failed to process match ratings: {error}")
            raise

    def _evaluate_individual(self, player: PlayerPerformance, roster_index: int) -> Dict[str, Any]:
        brawler_class = self._resolve_brawler_class(player.brawler)
        
        mechanical_score = self._skill_evaluator.evaluate(player, brawler_class)
        tactical_score = self._tactical_strategy.evaluate(player, mechanical_score)
        
        final_rating = self._apply_contextual_multipliers(player, tactical_score, brawler_class)
        
        return {
            "name": player.name,
            "brawler": player.brawler,
            "rating": self._enforce_rating_boundaries(final_rating, player.win_rate),
            "ksh": self._calculate_kill_share(player.average_kills, roster_index),
            "dvs_e": self._calculate_damage_differential(player.average_damage, brawler_class)
        }

    def _resolve_brawler_class(self, brawler_name: str) -> str:
        if brawler_name not in BRAWLERS_DATABASE:
            logger.warning(f"Unmapped Brawler detected: {brawler_name}. Defaulting to Hybrid.")
        return BRAWLERS_DATABASE.get(brawler_name, ["Hybrid"])[0]

    def _apply_contextual_multipliers(self, player: PlayerPerformance, base_score: float, brawler_class: str) -> float:
        win_modifier = 0.95 + (player.win_rate * 0.10)
        synergy_modifier = self._resolve_synergy_modifier(brawler_class)
        kit_modifier = self._resolve_kit_modifier(player.brawler)
        
        return base_score * win_modifier * synergy_modifier * kit_modifier

    def _resolve_synergy_modifier(self, brawler_class: str) -> float:
        synergy_matrix = {
            "Brawl Ball": {"Tank": 1.15},
            "Gem Grab": {"Support": 1.10, "Controller": 1.10},
            "Knockout": {"Tank": 1.15}
        }
        return synergy_matrix.get(self._normalized_mode, {}).get(brawler_class, 1.0)

    def _resolve_kit_modifier(self, brawler_name: str) -> float:
        kit_modifiers = {"Poco": 1.15, "Doug": 1.25}
        return kit_modifiers.get(brawler_name, 1.0)

    def _enforce_rating_boundaries(self, calculated_rating: float, win_rate: float) -> float:
        is_winner = win_rate > 0.5
        absolute_minimum = 1.02 if (is_winner and calculated_rating < 1.0) else 0.15
        return round(max(absolute_minimum, calculated_rating), 2)

    def _calculate_kill_share(self, player_kills: float, roster_index: int) -> float:
        is_team_one = roster_index < 3
        total_team_kills = self._baseline.retrieve_team_kills(is_team_one)
        
        if total_team_kills <= 0:
            return 33.3
        return round((player_kills / total_team_kills) * 100, 1)

    def _calculate_damage_differential(self, player_damage: float, brawler_class: str) -> float:
        expected_damage = self._skill_evaluator.get_expected_damage(brawler_class)
        safe_expected_damage = max(0.1, expected_damage)
        
        differential_ratio = (player_damage / safe_expected_damage) - 1
        return round(differential_ratio * 100, 1)
