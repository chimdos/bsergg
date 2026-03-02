# --- BSERgg Engine v1.0.0 ---
# Context-aware rating algorithm for Brawl Stars Esports.
# Developed by chimdos.

import numpy as np
from dataclasses import dataclass
from typing import List, Dict, Tuple

# --- Configuration & Data Maps ---

BRAWLER_ROSTER = {
    "8-BIT": ["DPS"], "Alli": ["Assassin"], "Amber": ["DPS"], "Angelo": ["Sniper"],
    "Ash": ["Tank"], "Barley": ["Thrower"], "Bea": ["Sniper", "Anti-Tank"],
    "Belle": ["Sniper"], "Berry": ["Support", "Thrower"], "Bibi": ["Tank"],
    "Bo": ["Controller"], "Bonnie": ["Sniper"], "Brock": ["Sniper"], "Bull": ["Tank"],
    "Buster": ["Tank"], "Buzz": ["Assassin", "Tank"], "Byron": ["Sniper", "Support"],
    "Carl": ["Assassin"], "Charlie": ["Anti-Tank"], "Chester": ["DPS"],
    "Chuck": ["Tank"], "Clancy": ["Anti-Tank"], "Colette": ["Anti-Tank"],
    "Colt": ["DPS"], "Cordelius": ["Assassin"], "Crow": ["Controller"],
    "Darryl": ["Assassin", "Tank"], "Doug": ["Tank"], "Draco": ["Tank"],
    "Dynamike": ["Thrower"], "Edgar": ["Assassin"], "El Primo": ["Tank"],
    "Emz": ["Anti-Tank"], "Eve": ["Controller"], "Fang": ["Assassin"],
    "Finx": ["Controller"], "Frank": ["Tank"], "Gale": ["Anti-Tank"],
    "Gene": ["Controller"], "Gigi": ["Assassin"], "Glowbert": ["Support"],
    "Gray": ["Support"], "Griff": ["Anti-Tank"], "Grom": ["Thrower"],
    "Gus": ["Sniper"], "Hank": ["Tank"], "Jacky": ["Tank"], "Jae-yong": ["Support"],
    "Janet": ["Controller"], "Jessie": ["Controller"], "Juju": ["Thrower"],
    "Kaze": ["Assassin"], "Kenji": ["Assassin"], "Kit": ["Support"],
    "L&L": ["Thrower"], "Leon": ["Assassin"], "Lily": ["Assassin"],
    "Lola": ["DPS"], "Lou": ["Anti-Tank"], "Lumi": ["Controller"],
    "Maisie": ["Anti-Tank"], "Mandy": ["Sniper"], "Max": ["Support"],
    "Meeple": ["Controller"], "Meg": ["Tank", "DPS"], "Melodie": ["Assassin"],
    "Mico": ["Assassin"], "Mina": ["Anti-Tank", "Assassin"], "Moe": ["Assassin"],
    "Mortis": ["Assassin"], "Mr. P": ["Controller"], "Nani": ["Sniper"],
    "Nita": ["Anti-Tank"], "Ollie": ["Tank"], "Otis": ["Anti-Tank", "Controller"],
    "Pam": ["Support"], "Pearl": ["DPS"], "Pierce": ["Sniper"], "Piper": ["Sniper"],
    "Penny": ["Controller"], "Poco": ["Support"], "R-T": ["Sniper"], "Rico": ["DPS"],
    "Rosa": ["Tank"], "Ruffs": ["Controller"], "Sam": ["Tank"], "Sandy": ["Controller"],
    "Shade": ["Assassin"], "Shelly": ["Anti-Tank"], "Spike": ["DPS"],
    "Sprout": ["Thrower"], "Squeak": ["Controller"], "Stu": ["Assassin"],
    "Surge": ["Anti-Tank"], "Tara": ["Anti-Tank"], "Tick": ["Thrower"],
    "Trunk": ["Tank"], "Willow": ["Thrower"], "Ziggy": ["Thrower"],
}

CLASS_WEIGHTS = {
    "Tank":       {"kills": 0.80, "dps": 1.50},
    "DPS":        {"kills": 0.70, "dps": 2.00},
    "Assassin":   {"kills": 1.85, "dps": 0.45},
    "Sniper":     {"kills": 1.45, "dps": 1.05},
    "Support":    {"kills": 0.90, "dps": 1.20},
    "Controller": {"kills": 1.15, "dps": 1.20},
    "Thrower":    {"kills": 1.20, "dps": 1.10},
    "Anti-Tank":  {"kills": 1.05, "dps": 1.70},
    "Hybrid":     {"kills": 1.20, "dps": 1.20},
}

MAP_ADJUSTMENTS = {
    "Super Beach": {"dps": 1.25, "kills": 1.45}, "Sunny Soccer": {"dps": 1.00, "kills": 1.00},
    "Deathcap Trap": {"dps": 1.10, "kills": 1.15}, "Undermine": {"dps": 1.15, "kills": 0.95},
    "Ring of Fire": {"dps": 1.80, "kills": 1.20}, "Pit Stop": {"dps": 1.35, "kills": 1.20},
    "Kaboom Canyon": {"dps": 1.10, "kills": 1.25}, "New Horizons": {"dps": 0.85, "kills": 1.20},
    "Goldarm Gulch": {"dps": 1.10, "kills": 1.05}, "Dry Season": {"dps": 0.95, "kills": 1.10},
    "Layer Cake": {"dps": 1.05, "kills": 1.15}, "Hideout": {"dps": 0.80, "kills": 0.45},
    "Shooting Star": {"dps": 0.85, "kills": 0.70}, "Gem Fort": {"dps": 1.25, "kills": 1.40},
    "Pinhole Punt": {"dps": 1.25, "kills": 0.90}, "Last Stop": {"dps": 1.15, "kills": 1.25},
    "Out in the Open": {"dps": 0.90, "kills": 1.10}, "Open Zone": {"dps": 1.55, "kills": 1.00},
    "Bridge Too Far": {"dps": 1.15, "kills": 1.25}, "Center Stage": {"dps": 1.55, "kills": 0.85},
    "Canal Grande": {"dps": 1.10, "kills": 1.20}, "Safe Zone": {"dps": 0.90, "kills": 1.60},
    "Open Business": {"dps": 1.65, "kills": 1.10}, "Hot Potato": {"dps": 1.50, "kills": 1.15},
    "Triple Dribble": {"dps": 1.30, "kills": 1.40}, "Sneaky Fields": {"dps": 1.25, "kills": 1.45},
    "Hard Rock Mine": {"dps": 1.15, "kills": 1.10}, "Crystal Arcade": {"dps": 1.20, "kills": 1.15},
    "Dueling Beetles": {"dps": 1.55, "kills": 1.10}, "Belle's Rock": {"dps": 1.00, "kills": 0.85},
    "Pinball Dreams": {"dps": 1.25, "kills": 1.30}, "Double Swoosh": {"dps": 1.20, "kills": 1.25},
}

MODE_DIVISORS = {
    "Heist": (400, 10.0), "Knockout": (190, 6.0), "Hot Zone": (350, 11.0),
    "Bounty": (250, 4.5), "Gem Grab": (280, 8.5), "Brawl Ball": (310, 10.5)
}

HEIST_BURNERS = ["Chuck", "Mico", "Berry", "Melodie", "Nita", "Kaze"]

# --- Domain Models ---

@dataclass
class PlayerPerformance:
    name: str
    brawler: str
    kills: int
    dps: float
    won: bool
    dts: int = 0  # Damage to Safe (Heist only)

@dataclass
class MatchContext:
    map_name: str
    game_mode: str
    series_score: str

# --- Logic Helper Functions ---

def get_brawler_class(brawler_name: str) -> str:
    """Returns the competitive class for a given brawler name."""
    return BRAWLER_ROSTER.get(brawler_name, ["Hybrid"])[0]

def get_base_divisors(game_mode: str) -> Tuple[float, float]:
    """Returns the (dps_divisor, kills_divisor) for the game mode."""
    return MODE_DIVISORS.get(game_mode, (250, 8.0))

def calculate_intensity_factor(players: List[PlayerPerformance], dps_limit: float, kills_limit: float) -> float:
    """Computes Lobby Intensity based on performance vs expected limits."""
    avg_dps = np.mean([player.dps for player in players])
    avg_kills = np.mean([player.kills for player in players])
    return ((avg_dps / dps_limit) + (avg_kills / kills_limit)) / 2

def get_series_multipliers(context: MatchContext) -> Tuple[int, float]:
    """Returns (number_of_games, kill_multiplier) based on series length."""
    is_long_series = any(score in context.series_score for score in ["2-1", "1-2"])
    number_of_games = 3 if is_long_series else 2

    if context.game_mode in ["Bounty", "Knockout"]:
        kill_multiplier = 1.25 if is_long_series else 1.0
    else:
        kill_multiplier = 1.5 if is_long_series else 1.0

    return number_of_games, kill_multiplier

def calculate_heist_impact(player: PlayerPerformance, match_avg_dts: float, total_safe_hp: float) -> float:
    """Specific normalization for Heist Safe damage."""
    relative_dts = player.dts / match_avg_dts if match_avg_dts > 0 else 1.0
    absolute_dts = player.dts / (total_safe_hp * 0.30)
    return (relative_dts * 0.30) + (absolute_dts * 0.60)

def apply_mode_bonuses(base_score: float, player: PlayerPerformance, game_mode: str) -> float:
    """Applies contextual bonuses depending on the game mode and brawler class."""
    brawler_class = get_brawler_class(player.brawler)
    bonus = 1.0

    if game_mode == "Brawl Ball":
        if brawler_class == "Tank": bonus = 1.35
        elif brawler_class == "Assassin": bonus = 1.15
    elif game_mode == "Gem Grab" and brawler_class in ["Support", "Controller", "Sniper"]:
        bonus = 1.10
    elif game_mode == "Knockout":
        if player.kills >= 5: bonus = 1.10
        if brawler_class == "Tank": bonus = 1.25
    
    return base_score * bonus

# --- Main Scorer Engine ---

def calculate_individual_rating(player: PlayerPerformance, context: MatchContext, goals: dict, match_averages: dict) -> float:
    """The central algorithm: Scales performance stats into a normalized rating."""
    brawler_class = get_brawler_class(player.brawler)
    weights = CLASS_WEIGHTS.get(brawler_class, CLASS_WEIGHTS["Hybrid"])

    # Normalization Step
    skill_kills = (player.kills / match_averages['kills'] * 0.40) + (player.kills / goals['kills'] * 0.60)
    skill_dps = (player.dps / match_averages['dps'] * 0.40) + (player.dps / goals['dps'] * 0.60)

    # Core Scoring Logic
    if context.game_mode == "Heist":
        dts_score = calculate_heist_impact(player, match_averages['dts'], goals['safe_hp'])
        if player.brawler in HEIST_BURNERS:
            score = ((skill_kills * 0.50 + skill_dps * 0.50) * 0.30) + (dts_score * 0.70)
        else:
            score = ((skill_kills * weights['kills'] + skill_dps * weights['dps']) / 
                     (weights['kills'] + weights['dps']) * 0.70) + (dts_score * 0.30)
    elif context.game_mode in ["Knockout", "Bounty"]:
        kill_weight = 0.80 if context.game_mode == "Knockout" else 0.85
        score = (skill_kills * kill_weight) + (skill_dps * (1 - kill_weight))
    else:
        score = (skill_kills * weights['kills'] + skill_dps * weights['dps']) / (weights['kills'] + weights['dps'])

    # Application of situational multipliers
    rating = apply_mode_bonuses(score, player, context.game_mode)
    if player.won: rating *= 1.20
    if player.brawler == "Doug": rating *= 1.25

    # Impact threshold for winners
    if player.won and rating < 1.0 and player.dps > (match_averages['dps'] * 0.60):
        rating = 1.02

    return round(rating, 2)

def get_match_ratings(performances: List[PlayerPerformance], context: MatchContext) -> List[Dict]:
    """Orchestrates the rating calculation for an entire match lobby."""
    map_adj = MAP_ADJUSTMENTS.get(context.map_name, {"dps": 1.0, "kills": 1.0})
    base_dps_div, base_kills_div = get_base_divisors(context.game_mode)

    # Dynamic Goal Calculation
    raw_goal_dps = base_dps_div * map_adj['dps']
    raw_goal_kills = base_kills_div * map_adj['kills']

    intensity = calculate_intensity_factor(performances, raw_goal_dps, raw_goal_kills)
    number_of_games, kill_multiplier = get_series_multipliers(context)

    goals = {
        "dps": raw_goal_dps * (intensity ** 0.50),
        "kills": (raw_goal_kills * kill_multiplier) * (intensity / 1.10),
        "safe_hp": 80000 * number_of_games
    }

    match_averages = {
        "dps": np.mean([p.dps for p in performances]),
        "kills": np.mean([p.kills for p in performances]),
        "dts": np.mean([p.dts for p in performances]) if context.game_mode == "Heist" else 0
    }

    return [
        {
            "name": player.name,
            "brawler": player.brawler,
            "rating": calculate_individual_rating(player, context, goals, match_averages),
        }
        for player in performances
    ]

# --- Entry Point (Analysis Wrapper) ---

def run_analysis(dataset: List[Dict]):
    """Processes a raw dataset into a clean rating report."""
    for entry in dataset:
        players = [
            PlayerPerformance(
                name=p['name'],
                brawler=p['brawler'],
                kills=p['kills'],
                dps=p['dps'],
                won=p['win'],
                dts=p.get('dts', 0)
            ) for p in entry['players']
        ]

        context = MatchContext(
            map_name=entry['mapa'], 
            game_mode=entry['modo'], 
            series_score=entry['confronto']
        )

        results = get_match_ratings(players, context)

        print(f"\n--- Results: {context.series_score} | {context.map_name} ---")
        for res in results:
            print(f"Player: {res['name']:<12} | Brawler: {res['brawler']:<12} | Rating: {res['rating']}")
