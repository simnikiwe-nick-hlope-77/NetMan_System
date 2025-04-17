# TRACKING PROGRESS AND CHANGES
## CHANGELOG.md

All notable changes to the **NetMan_System** project will be documented in this file.

---

## [v1.0.0] - 2025-04-16

### Added
- Implemented all six creational design patterns in `/creational_patterns/`:
  - **Simple Factory** for network devices (Router, Switch, Firewall)
  - **Factory Method** for alert processors (Email, SMS)
  - **Abstract Factory** for platform-specific UI components (Windows, Linux)
  - **Builder** for constructing complex network configurations
  - **Prototype** for cloning reusable network templates
  - **Singleton** to ensure a single instance of `NetworkMonitor`

- Created unit tests in `/tests/test_patterns.py`:
  - Validated correct object creation for all patterns
  - Handled edge cases (invalid input, cloning, singleton behavior)

- Added coverage report in Markdown format (`/tests/coverage_report.md`):
  - Achieved **100% test coverage** across all pattern modules

### Updated
- Refactored class structures to align with design patterns
- Modularized code into organized, pattern-specific files
- Enhanced readability with full docstring comments

### Documentation
- Added clear inline comments to all creational pattern files
- Created:
  - `README.md` (in progress)
  - `coverage_report.md`
  - `CHANGELOG.md` (this file)

---

> Maintained by: NetMan_System Development Team
