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

## Roadmap

We are currently refactoring the core logic to follow **Clean Code** principles, ensuring the engine is ready for community contributions and professional integration.

- [ ] **Core Engine:** Pure mathematical functions for rating calculations.
- [ ] **Data Adapters:** Seamless integration with official Brawl Stars API JSON outputs.
- [ ] **Public API Vision:** Transforming the engine into a service that websites like Brawlify or competitive hubs can integrate via a public API.

---

## Tech Stack

* **Language:** Python 3.10+
* **Math & Analytics:** NumPy (High-performance distribution analysis)
* **Architecture:** Modular design using Dataclasses and abstractions.

---

## Stay Tuned

Developed by **Daniel "chimdos" Martins**. 

The code is being polished and will be public soon.