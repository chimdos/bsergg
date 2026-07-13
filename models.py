from dataclasses import dataclass
from typing import List

@dataclass(frozen=True)
class PlayerPerformance:
    tag: str
    name: str
    brawler: str
    average_kills: float
    average_deaths: float
    average_damage: float
    average_damage_to_safe: float
    win_rate: float

@dataclass(frozen=True)
class MatchContext:
    mode: str
    map_name: str
    is_long_series: bool
    players: List[PlayerPerformance]

    def resolve_normalized_mode(self) -> str:
        raw_mode = str(self.mode).lower().replace(" ", "")
        normalization_map = {
            "heist": "Heist",
            "brawlball": "Brawl Ball",
            "gemgrab": "Gem Grab",
            "knockout": "Knockout",
            "bounty": "Bounty",
            "hotzone": "Hot Zone",
            "wipeout": "Wipeout"
        }
        return normalization_map.get(raw_mode, "Unknown")