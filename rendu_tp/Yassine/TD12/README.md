# TD12 - Integration + Release

## Objective

Prepare MarketPulse for a reproducible final release by cleaning the repository, documenting installation and execution, validating both application paths, and reviewing the final integration.

## Scope

- Confirm the final provider or access mode.
- Verify repository cleanliness.
- Verify direct dependencies in `requirements.txt`.
- Ensure README instructions are accurate.
- Validate the terminal application.
- Validate the Dash dashboard.
- Verify the shared market snapshot architecture.
- Prepare final integration and review.
- Prepare Checkpoint C evidence.

## Application Commands

Install dependencies:

```bash
python -m pip install -r requirements.txt
```

Run the terminal application:

```bash
python src/main.py
```

Run the dashboard:

```bash
python src/dashboard.py
```

## Architecture

The application follows the shared snapshot architecture:

```text
Provider
    ↓
Canonical Market Data
    ↓
Analytics
    ↓
build_market_snapshot()
    ↓
Terminal Application / Dash Dashboard
```

The dashboard consumes the shared snapshot and does not implement provider acquisition or financial calculations.

## Validation

The terminal and dashboard execution paths are tested independently.

The final validation must confirm:
- Provider and access mode are documented honestly.
- Instrument and benchmark are correct.
- Lookback and interval are displayed.
- Instrument return is displayed.
- Benchmark return is displayed.
- Relative performance is displayed.
- Both Base 100 series are displayed.
- No secrets are committed.
- Dependencies are documented.
- The repository can be reproduced using documented instructions.

## Evidence

Screenshots are stored in the `captures/` directory.

