# Changelog

All notable changes to this project will be documented in this file. This project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.3.0] - 2026-07-13

### Added
- **SOLID Architecture & Strategy Pattern**: Complete structural refactoring of `engine.py`. Introduced Dependency Inversion (`IRatingStrategy`) to isolate mode-specific tactical scoring from core mechanical evaluations.
- **Data Encapsulation**: Strict separation of concerns in `models.py`. Data structures (`PlayerPerformance`, `MatchContext`) now expose only data and encapsulate behavior, adhering to Clean Code guidelines.
- **Mode Normalization**: Implemented a robust string sanitization method (`resolve_normalized_mode`) to safely map unpredictable API strings to strict internal constants.

### Changed
- **Heist Tactical Overhaul**: Replaced the previous binary Heist calculation with a comprehensive 3-tier evaluation system.
  - *Kamikazes/Burners* (e.g., Chuck, Mico) now use a balanced 60/40 mechanical-to-objective weight to account for PvE-heavy playstyles.
  - *Defenders* now face a 0.90x base multiplier, requiring baseline objective damage (or exceptional PvP dominance) to avoid rating penalties.
- **Objective Benchmarks**: Increased the Heist objective damage benchmark from 15% to 25% of the Safe's HP.
- **Hard Caps**: Instituted a strict `2.0x` ceiling on the `objective_ratio` to completely eliminate infinite rating inflation from hyper-aggressive objective rushes.

### Fixed
- **Heist Logic Bypass**: Resolved a critical string-casing exception that silently disabled the Heist matrix in previous patches, ensuring objective modifiers are now perfectly applied.

## [1.1.1] - 2026-04-20

### Added
- **New Brawlers Support**: Added Najia to the roster.
- **Archetype Refinement**: Updated several Brawlers' classes

### Changed
- **Class Weights**: Tweaked `CLASS_BASE_WEIGHTS` for better precision in damage-to-kill ratios.

## [1.1.0] - 2026-04-18

### Added
- **Modular Architecture**: Split the project into `engine.py`, `constants.py`, and `models.py` for better maintainability.
- **Dynamic Normalization**: Introduced `match_pace_modifier` to adjust ratings based on lobby intensity.
- **New Metrics**: Added `ksh` (Kill Share) and `dvs_e` (Damage vs Expected %) to the output report.
- **Heist Logic**: Implemented specific handling for "Heist Burners" with 70% weight on Safe Damage.

### Changed
- Refactored core logic from standalone functions to the `BSERRatingEngine` class.
- Externalized brawler data and map multipliers to `constants.py`.

### Fixed
- Improved calculation fairness for support classes using power-curve normalization.

## [1.0.0] - 2026-03-10
### Added
- Initial private research version (Google Colab).
- Basic DPS and Kill normalization.