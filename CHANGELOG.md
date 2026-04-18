# Changelog

All notable changes to this project will be documented in this file. This project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

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