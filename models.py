"""
Determines how the data flows through the Engine
"""

from dataclasses import dataclass
from typing import List

@dataclass
class PlayerSession:
    name: str
    brawler: str
    kills: int
    dps: float
    won: bool
    damage_to_safe: int = 0

@dataclass
class MatchContext:
    map_name: str
    mode: str
    series_score: str
    players: List[PlayerSession]