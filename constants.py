"""
Static configuration and references data
Incudes brawler archetypes, class weights and map-specific adjustments
"""

BRAWLER_ROSTER = {
    "8-BIT": ["DPS"], "Alli": ["Assassin"], "Amber": ["Controller", "DPS"], "Angelo": ["Sniper"],
    "Ash": ["Tank"], "Barley": ["Thrower"], "Bea": ["Sniper"],
    "Belle": ["Sniper"], "Berry": ["Support"], "Bibi": ["Tank"],
    "Bo": ["Controller"], "Bonnie": ["Controller"], "Brock": ["Sniper"], "Bull": ["Tank"],
    "Buster": ["Tank"], "Buzz": ["Assassin", "Tank"], "Byron": ["Sniper"],
    "Carl": ["Assassin"], "Charlie": ["Anti-Tank"], "Chester": ["DPS"],
    "Chuck": ["Tank"], "Clancy": ["Anti-Tank"], "Colette": ["Anti-Tank"],
    "Colt": ["DPS"], "Cordelius": ["Anti-Tank"], "Crow": ["Controller", "Anti-Tank"],
    "Darryl": ["Assassin"], "Doug": ["Tank"], "Draco": ["Tank"],
    "Dynamike": ["Thrower"], "Edgar": ["Assassin"], "El Primo": ["Tank"],
    "Emz": ["Anti-Tank"], "Eve": ["Controller"], "Fang": ["Assassin", "Tank"],
    "Finx": ["Controller", "Anti-Tank"], "Frank": ["Tank"], "Gale": ["Anti-Tank"],
    "Gene": ["Controller"], "Gigi": ["Assassin"], "Glowbert": ["Support"],
    "Gray": ["Support"], "Griff": ["Anti-Tank"], "Grom": ["Thrower"],
    "Gus": ["Sniper"], "Hank": ["Tank"], "Jacky": ["Tank"], "Jae-yong": ["Support"],
    "Janet": ["Controller"], "Jessie": ["Controller"], "Juju": ["Thrower"],
    "Kaze": ["Assassin"], "Kenji": ["Tank"], "Kit": ["Support"],
    "L&L": ["Thrower"], "Leon": ["Assassin"], "Lily": ["Assassin"],
    "Lola": ["DPS"], "Lou": ["Anti-Tank"], "Lumi": ["Controller", "Anti-Tank"],
    "Maisie": ["Anti-Tank"], "Mandy": ["Sniper"], "Max": ["Support"],
    "Meeple": ["Controller"], "Meg": ["DPS"], "Melodie": ["Assassin"],
    "Mico": ["Assassin"], "Mina": ["Assassin"], "Moe": ["Assassin"],
    "Mortis": ["Assassin"], "Mr. P": ["Controller"], "Najia": ["Controller"], "Nani": ["Sniper"],
    "Nita": ["Anti-Tank"], "Ollie": ["Tank"], "Otis": ["Anti-Tank"],
    "Pam": ["Controller"], "Pearl": ["DPS"], "Pierce": ["Sniper"], "Piper": ["Sniper"], "Penny" : ["Controller"],
    "Poco": ["Support"], "R-T": ["Sniper"], "Rico": ["DPS"], "Rosa": ["Tank"],
    "Ruffs": ["Controller", "Anti-Tank"], "Sam": ["Tank"], "Sandy": ["Controller"],
    "Shade": ["Assassin"], "Shelly": ["Anti-Tank"], "Sirius": ["Thrower"], "Spike": ["DPS"],
    "Sprout": ["Thrower"], "Squeak": ["Controller"], "Stu": ["Controller"],
    "Surge": ["Anti-Tank"], "Tara": ["Anti-Tank"], "Tick": ["Thrower"],
    "Trunk": ["Tank"], "Willow": ["Thrower"], "Ziggy": ["Thrower"]
}

CLASS_BASE_WEIGHTS = {
    "Tank":       {"kills": 0.90, "dps": 1.25},
    "DPS":        {"kills": 1.00, "dps": 1.50},
    "Assassin":   {"kills": 1.30, "dps": 0.80},
    "Sniper":     {"kills": 1.10, "dps": 1.35},
    "Support":    {"kills": 0.90, "dps": 1.10},
    "Controller": {"kills": 1.10, "dps": 1.20},
    "Thrower":    {"kills": 1.00, "dps": 1.30},
    "Anti-Tank":  {"kills": 1.10, "dps": 1.40},
    "Hybrid":     {"kills": 1.15, "dps": 1.30},
}

CLASS_EXPECTED_OUTPUT = {
    "Tank": 1.15, "DPS": 1.45, "Assassin": 1.10, "Sniper": 1.20, 
    "Support": 0.85, "Controller": 1.05, "Thrower": 1.10, 
    "Anti-Tank": 1.30, "Hybrid": 1.15
}

MODE_EXPECTATION_MATRIX = {
    "Knockout": {"Tank": 0.45, "Assassin": 0.55, "Sniper": 1.0, "Support": 0.70, "DPS": 0.85, "Anti-Tank": 0.80},
    "Bounty":   {"Tank": 0.50, "Assassin": 0.65, "Sniper": 1.0, "Support": 0.75, "DPS": 0.85, "Anti-Tank": 0.80},
    "Heist":    {"Tank": 1.30, "Assassin": 1.10, "Sniper": 0.85},
    "Brawl Ball": {"Tank": 1.15, "Assassin": 1.05}
}

MODE_BASE_DIVISORS = {
    "Heist": (340, 7.5), "Knockout": (130, 4.0), "Hot Zone": (280, 8.0),
    "Bounty": (170, 4.0), "Gem Grab": (230, 6.5), "Brawl Ball": (240, 7.5)
}

MAP_MULTIPLIERS = {
    "Super Beach": {"dps": 1.15, "kills": 1.30},
    "Sunny Soccer": {"dps": 1.00, "kills": 1.00},
    "Deathcap Trap":      {"dps": 1.10, "kills": 1.15},
    "Undermine":          {"dps": 1.15, "kills": 0.95},
    "Ring of Fire":       {"dps": 1.75, "kills": 1.10},
    "Pit Stop":           {"dps": 1.35, "kills": 1.20},
    "Kaboom Canyon":      {"dps": 1.10, "kills": 1.25},
    "New Horizons":       {"dps": 0.85, "kills": 1.20},
    "Goldarm Gulch":      {"dps": 1.10, "kills": 1.05},
    "Dry Season":         {"dps": 0.95, "kills": 1.10},
    "Layer Cake":         {"dps": 1.05, "kills": 1.15},
    "Hideout":            {"dps": 0.80, "kills": 0.45},
    "Shooting Star":      {"dps": 0.85, "kills": 0.70},
    "Gem Fort":           {"dps": 1.25, "kills": 1.40},
    "Pinhole Punt":       {"dps": 1.25, "kills": 0.90},
    "Last Stop":          {"dps": 1.15, "kills": 1.25},
    "Out in the Open":    {"dps": 0.90, "kills": 1.10},
    "Open Zone":          {"dps": 1.55, "kills": 1.00},
    "Bridge Too Far":     {"dps": 0.90, "kills": 0.85},
    "Last Stop":          {"dps": 1.15, "kills": 0.75},
    "Center Stage":       {"dps": 1.55, "kills": 0.85},
    "Canal Grande":       {"dps": 1.10, "kills": 1.20},
    "Safe Zone":          {"dps": 0.95, "kills": 1.55},
    "Open Business":      {"dps": 1.65, "kills": 1.10},
    "Hot Potato":         {"dps": 1.50, "kills": 1.15},
    "Triple Dribble":     {"dps": 1.30, "kills": 1.40},
    "Sneaky Fields":      {"dps": 1.25, "kills": 1.45},
    "Hard Rock Mine":     {"dps": 1.10, "kills": 1.05},
    "Crystal Arcade":     {"dps": 1.20, "kills": 1.15},
    "Dueling Beetles":    {"dps": 1.55, "kills": 1.10},
    "Belle's Rock":       {"dps": 1.00, "kills": 0.85},
    "Pinball Dreams":     {"dps": 1.25, "kills": 1.30},
    "Double Swoosh":      {"dps": 1.20, "kills": 1.25},
}

HEIST_BURNING_BRAWLERS = ["Chuck", "Mico", "Berry", "Melodie", "Nita", "Kaze"]