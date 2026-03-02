# BSERgg: The Competitive Rating Engine

> "Context is the difference between a high stat and a high-impact performance."

BSERgg is an advanced, context-aware analytical engine designed to quantify player performance in the Brawl Stars esports scene. 

This repository marks the transition of the BSERgg algorithm from a private research environment (Google Colab) into a modular, and open-source Python library.

---

## The Philosophy

In competitive gaming, flat statistics (like total kills or total damage) fail to tell the whole story. BSERgg moves away from "flat benchmarks" and introduces **Dynamic Performance Normalization**.

The engine evaluates players not against an arbitrary number, but against the **Lobby Intensity**. 

### Key Features (Teaser)

* **Dynamic Normalization:** Ratings are scaled based on the match's average DPS and Kills. If the game is slow, the bar adjusts. If it's a bloodbath, the requirements for the MVP status rise.
* **Role-Based Weighting:** A Sniper's impact is measured differently than a Tank's. The engine automatically applies weights based on the Brawler's competitive class.
* **Intensity Scaling:** The algorithm detects the pace of the match and the series length (e.g., a high-stakes 2-1 set) to adjust performance multipliers.
* **Heist-Burner Detection:** Specific logic for Heist mode that balances Damage to Safe (DTS) with map control performance.

---

## Getting Started

### Prerequisites
* Python 3.10 or higher.
* NumPy library.

### Installation
1. Clone this repository:
   git clone https://github.com/your-username/bsergg-engine.git
   cd bsergg-engine

2. Set up a virtual environment:
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate

3. Install dependencies:
   pip install -r requirements.txt

### Quick Usage
```python
from engine import PlayerPerformance, MatchContext, get_match_ratings

players = [
    PlayerPerformance(name="Sitetampo", brawler="Frank", kills=12, dps=450.0, won=True)
]
context = MatchContext(map_name="Super Beach", game_mode="Brawl Ball", series_score="2-0")

results = get_match_ratings(players, context)
print(results)
```

---

## Roadmap

We are currently refactoring the core logic to follow **Clean Code** principles, ensuring the engine is ready for community contributions and professional integration.

- [x] **Core Engine:** Pure mathematical functions for rating calculations.
- [ ] **Data Adapters:** Seamless integration with official Brawl Stars API JSON outputs.
- [ ] **Public API Vision:** Transforming the engine into a service that websites like Brawlify or competitive hubs can integrate via a public API.

---

## Rights & Licensing

This project is part of the **BSERgg** ecosystem. By open-sourcing the engine, we aim to provide the Brawl Stars community with a standardized, transparent, and context-aware method to measure competitive performance.

* **Community Use:** You are free to use this engine for personal projects, community-run tournaments, and academic research.
* **Commercial Integrations:** If you intend to integrate this algorithm into a commercial platform, mobile app, or high-traffic website (e.g., global stat trackers), please contact the author for proper attribution and integration support.
* **License:** This project is distributed under the MIT License. See the `LICENSE` file for more details.

**BSERgg** and its logic are developed by **Daniel "chimdos" Martins**.

---

## Tech Stack

* **Language:** Python 3.10+
* **Math & Analytics:** NumPy (High-performance distribution analysis)
* **Architecture:** Modular design using Dataclasses and abstractions.

---

Developed by **Daniel "chimdos" Martins**. 
