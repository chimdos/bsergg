<h1 align="center">BSERgg: The Competitive Rating Engine</h1>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10%2B-blue" alt="Python 3.10+" />
  <img src="https://img.shields.io/badge/License-MIT-green" alt="License MIT" />
  <img src="https://img.shields.io/badge/Status-Active-success" alt="Status Active" />
</p>

BSERgg is an advanced, context-aware analytical engine designed to quantify player performance in the Brawl Stars esports scene.

This repository contains the core mathematical logic and architecture of the BSERgg algorithm, transitioned from a private research environment into a modular, open-source Python library.

---

## Table of Contents

<details>
<summary>Click to expand</summary>

1. [The Philosophy](#the-philosophy)
2. [Key Features](#key-features)
3. [Getting Started](#getting-started)
   - [Prerequisites](#prerequisites)
   - [Installation](#installation)
   - [Quick Usage](#quick-usage)
4. [Roadmap](#roadmap)
5. [Contributing](#contributing)
6. [Rights & Licensing](#rights--licensing)
7. [Tech Stack](#tech-stack)

</details>

---

## The Philosophy

In competitive gaming, flat statistics (like total kills or total damage) fail to tell the whole story. BSERgg moves away from flat benchmarks and introduces **Dynamic Performance Normalization**.

The engine evaluates players not against an arbitrary number, but against the actual **Lobby Intensity**. It takes into account what brawler class is being played, the game mode, and the average output of all players in that specific match to generate a fair and accurate rating.

---

## Key Features

The engine has been entirely refactored to use modular, class-based architecture with dependency injection for mode-specific strategies.

* **Match Baseline Normalization:** Calculates the mean damage and mean kills of the specific lobby. Players are evaluated against the reality of the match they just played, not a static global average.
* **Mechanical Skill Evaluation:** Utilizes non-linear elastic power curves to calculate mechanical scores. This penalizes extreme statistical padding while rewarding consistent, high-impact scaling based on class expectations.
* **Tactical Mode Strategies:** Implements the Strategy Pattern for game modes. For example, the Heist strategy mathematically separates Safe Burners from Defenders based on their Objective Ratio and Damage to Safe (DTS).
* **Contextual Modifiers:** Automatically applies multipliers based on team synergy (e.g., Tank presence in Brawl Ball), specific brawler kit modifiers (e.g., Poco, Doug), and the overall win rate.
* **Advanced Output Metrics:** Generates detailed match reports including the normalized final Rating, Kill Share (KSH%), and Damage vs. Expected (DvsE%).

---

## Getting Started

### Prerequisites

* Python 3.10 or higher.
* NumPy library.

### Installation

1. Clone this repository:

    ```bash
    git clone https://github.com/chimdos/bsergg.git
    cd bsergg
    ```

2. Set up a virtual environment:

    ```bash
    python -m venv .venv
    source .venv/bin/activate  # On Windows use: .venv\Scripts\activate
    ```

3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

### Quick Usage

The engine requires manual passing of match parameters and player data, making it flexible for any data entry method. Here is a minimal example of how to process a match:

```python
from models import PlayerPerformance, MatchContext
from engine import BSERRatingEngine

# 1. Define the players and their raw statistics
players_data = [
    PlayerPerformance(name="Sitetampo", brawler="Frank", average_kills=12.0, average_damage=45000.0, average_damage_to_safe=0.0, win_rate=1.0),
    PlayerPerformance(name="Kenji", brawler="Poco", average_kills=3.0, average_damage=25000.0, average_damage_to_safe=0.0, win_rate=1.0),
    # ... Add all 6 players from the match ...
]

# 2. Set the match context
context = MatchContext(
    map_name="Super Beach",
    game_mode="Brawl Ball",
    series_score="2-0",
    players=players_data
)

# 3. Initialize the engine and process ratings
engine = BSERRatingEngine(context)
results = engine.process_match_ratings()

# 4. Output the results
for res in results:
    print(f"Player: {res['name']} ({res['brawler']})")
    print(f"Rating: {res['rating']} | KSH: {res['ksh']}% | DvsE: {res['dvs_e']}%")
    print("-" * 30)
```

---

## Roadmap

The BSERgg ecosystem is expanding beyond just the mathematical engine. Our current trajectory includes:

* [x] **Core Engine Refactoring:** Pure mathematical functions, Clean Code architecture, and dependency injection for rating calculations.
* [ ] **Global Team Rankings:** Expanding the algorithm to evaluate and rank professional teams based on aggregate roster performance.
* [ ] **Official Website Launch:** A public-facing web platform to view calculated ratings and match histories.
* [ ] **Moneybrawl Scouting System:** An advanced analytical hub to help organizations scout undervalued talent using BSERgg's context-aware metrics.

---

## Contributing

We welcome community contributions to improve the mathematical models, add new mode strategies, or optimize the architecture.

Please read the `CONTRIBUTING.md` file for details on our code of conduct and the process for submitting pull requests.

---

## Rights & Licensing

This project is part of the BSERgg ecosystem. By open-sourcing the engine, we aim to provide the Brawl Stars community with a standardized, transparent, and context-aware method to measure competitive performance.

* **Community Use:** You are free to use this engine for personal projects, community-run tournaments, and academic research.
* **Commercial Integrations:** If you intend to integrate this algorithm into a commercial platform, mobile app, or high-traffic website, please contact the author for proper attribution and integration support.
* **License:** This project is distributed under the MIT License. See the `LICENSE` file for more details.

---

## Tech Stack

* **Language:** Python 3.10+
* **Math & Analytics:** NumPy (High-performance distribution analysis)
* **Architecture:** Modular Object-Oriented Design (Strategy Pattern, Dependency Injection, Dataclasses)
