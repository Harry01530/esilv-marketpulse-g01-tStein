# MarketPulse

MarketPulse is a Python market-comparison application that evaluates an equity instrument against a benchmark index over a 1-month daily window using canonical OHLCV series, shared analytics, a terminal report, and an interactive Dash dashboard.

## Market Configuration

- **Instrument:** `AAPL` — Apple Inc.
- **Benchmark:** `SP500` — S&P 500
- **Lookback:** 1 month
- **Interval:** Daily

## Active Provider & Access Mode

- **Provider:** Bloomberg stage
- **Access mode:** `APPROVED_SAMPLE`
- **Mapping contract:** `docs/BLOOMBERG_FIELD_MAPPING.md` (`AAPL -> AAPL US Equity`, `SP500 -> SPX Index`)

## Environment Constraints

- Live Bloomberg Terminal (`blpapi`) connectivity is **not** required or demonstrated in this release.
- Data is loaded from the instructor-approved fallback fixture `data/sample/bloomberg_reference_sample.json` and normalized at the provider boundary (`src/providers/bloomberg_provider.py`) before reaching `src/analytics.py`.
- All commands must be executed from the repository root directory.

## Installation

Create and activate a virtual environment, then install direct dependencies:

```bash
python -m pip install -r requirements.txt