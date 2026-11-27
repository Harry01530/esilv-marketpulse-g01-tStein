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
- The optional Yahoo provider (`src/providers/yahoo_provider.py`) requires internet access.
- All commands must be executed from the repository root directory.

## Installation

Install direct dependencies:

```bash
python -m pip install -r requirements.txt
```

## Run

Terminal report:

```bash
python src/main.py
```

Dash dashboard (then open http://127.0.0.1:8050, stop with Ctrl+C):

```bash
python src/dashboard.py
```

## Architecture

```text
provider (Bloomberg stage)
        |
        v
canonical rows (date, ticker, open, high, low, close, volume)
        |
        v
src/analytics.py
        |
        v
build_market_snapshot() in src/main.py
        |
        +-------------------+
        v                   v
terminal (main.py)    dashboard (dashboard.py)
```

## Evidence

Checkpoint evidence is stored under `evidence/checkpoint-<letter>/<github-username>/`.