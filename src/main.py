from pathlib import Path
import json

from analytics import (
    align_series,
    calculate_base_100,
    calculate_period_return,
    calculate_relative_performance,
)
from providers.yahoo_provider import YAHOO_SYMBOLS, fetch_yahoo_prices

# Chemins des fichiers
ROOT_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT_DIR / "data" / "sample"

# Configuration
PROVIDER_LABEL = "Yahoo Finance via yfinance"
PERIOD = "1mo"
INTERVAL = "1d"
LOOKBACK_LABEL = "1 month"
INTERVAL_LABEL = "Daily"


def load_instruments():
    with open(DATA_DIR / "instruments.json", encoding="utf-8") as file:
        return json.load(file)


def main():
    # 1. Métadonnées des instruments (tickers canoniques)
    instruments = load_instruments()
    instrument = instruments["instrument"]
    benchmark = instruments["benchmark"]

    # 2. Récupération Yahoo (lignes canoniques)
    instrument_prices = fetch_yahoo_prices(
        symbol=YAHOO_SYMBOLS[instrument["ticker"]],
        canonical_ticker=instrument["ticker"],
        period=PERIOD,
        interval=INTERVAL,
    )

    benchmark_prices = fetch_yahoo_prices(
        symbol=YAHOO_SYMBOLS[benchmark["ticker"]],
        canonical_ticker=benchmark["ticker"],
        period=PERIOD,
        interval=INTERVAL,
    )

    # 3. Alignement des dates communes (TD07)
    aligned_instrument, aligned_benchmark = align_series(
        instrument_prices,
        benchmark_prices,
    )

    if not aligned_instrument or not aligned_benchmark:
        raise ValueError("No common dates between instrument and benchmark")

    # 4. Calculs (TD07, inchangés)
    instrument_return = calculate_period_return(aligned_instrument)
    benchmark_return = calculate_period_return(aligned_benchmark)

    relative_performance = calculate_relative_performance(
        instrument_return,
        benchmark_return,
    )

    instrument_base_100 = calculate_base_100(aligned_instrument)
    benchmark_base_100 = calculate_base_100(aligned_benchmark)

    # 5. Affichage
    print("=== MarketPulse ===\n")

    print("Provider")
    print(PROVIDER_LABEL)

    print("\nMarket configuration")
    print(f"Period   : {LOOKBACK_LABEL}")
    print(f"Interval : {INTERVAL_LABEL}")

    print("\nInstrument")
    print(f"{instrument['ticker']} - {instrument['name']}")
    print(f"Observations  : {len(aligned_instrument)}")
    print(f"First date    : {aligned_instrument[0]['date']}")
    print(f"Last date     : {aligned_instrument[-1]['date']}")
    print(f"Period return : {instrument_return:.2f}%")

    print("\nBenchmark")
    print(f"{benchmark['ticker']} - {benchmark['name']}")
    print(f"Observations  : {len(aligned_benchmark)}")
    print(f"Period return : {benchmark_return:.2f}%")

    print("\nRelative performance")
    print(
        f"{instrument['ticker']} vs {benchmark['ticker']} : "
        f"{relative_performance:+.2f} percentage points"
    )

    print("\nBase 100")
    print(
        f"{instrument['ticker']} : "
        f"{instrument_base_100[0]['value']:.2f} -> "
        f"{instrument_base_100[-1]['value']:.2f}"
    )
    print(
        f"{benchmark['ticker']} : "
        f"{benchmark_base_100[0]['value']:.2f} -> "
        f"{benchmark_base_100[-1]['value']:.2f}"
    )


if __name__ == "__main__":
    main()