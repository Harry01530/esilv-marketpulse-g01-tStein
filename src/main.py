from pathlib import Path
import csv
import json

from analytics import (
    align_series,
    calculate_base_100,
    calculate_period_return,
    calculate_relative_performance,
)

DATA_DIR = Path(__file__).resolve().parent.parent / "data" / "sample"

PROVIDER_LABEL = "Local sample data"
ACCESS_MODE = "Offline / sample dataset"
LOOKBACK_LABEL = "1 month"
INTERVAL_LABEL = "Daily"


def load_instruments():
    with open(DATA_DIR / "instruments.json", encoding="utf-8") as file:
        return json.load(file)


def load_prices():
    with open(DATA_DIR / "prices.csv", encoding="utf-8") as file:
        prices = list(csv.DictReader(file))

    for row in prices:
        row["close"] = float(row["close"])

    return prices


def filter_prices(prices, ticker):
    return [row for row in prices if row["ticker"] == ticker]


def build_market_snapshot():
    instruments = load_instruments()
    prices = load_prices()

    instrument = instruments["instrument"]
    benchmark = instruments["benchmark"]

    instrument_prices = filter_prices(prices, instrument["ticker"])
    benchmark_prices = filter_prices(prices, benchmark["ticker"])

    aligned_instrument, aligned_benchmark = align_series(
        instrument_prices,
        benchmark_prices,
    )

    if not aligned_instrument or not aligned_benchmark:
        raise ValueError("No common dates between instrument and benchmark")

    instrument_return = calculate_period_return(aligned_instrument)
    benchmark_return = calculate_period_return(aligned_benchmark)

    return {
        "provider": PROVIDER_LABEL,
        "access_mode": ACCESS_MODE,
        "lookback": LOOKBACK_LABEL,
        "interval": INTERVAL_LABEL,
        "instrument": instrument,
        "benchmark": benchmark,
        "instrument_return": instrument_return,
        "benchmark_return": benchmark_return,
        "relative_performance": calculate_relative_performance(
            instrument_return,
            benchmark_return,
        ),
        "instrument_base_100": calculate_base_100(aligned_instrument),
        "benchmark_base_100": calculate_base_100(aligned_benchmark),
    }


def main():
    snapshot = build_market_snapshot()

    instrument = snapshot["instrument"]
    benchmark = snapshot["benchmark"]

    instrument_base_100 = snapshot["instrument_base_100"]
    benchmark_base_100 = snapshot["benchmark_base_100"]

    print("=== MarketPulse ===\n")

    print("Provider")
    print(f"{snapshot['provider']}\n")

    print("Access mode")
    print(f"{snapshot['access_mode']}\n")

    print("Market configuration")
    print(f"Instrument : {instrument['ticker']} - {instrument['name']}")
    print(f"Benchmark  : {benchmark['ticker']} - {benchmark['name']}")
    print(f"Period     : {snapshot['lookback']}")
    print(f"Interval   : {snapshot['interval']}\n")

    print(f"Instrument return : {snapshot['instrument_return']:+.2f}%")
    print(f"Benchmark return  : {snapshot['benchmark_return']:+.2f}%\n")

    print("Relative performance")
    print(
        f"{instrument['ticker']} vs {benchmark['ticker']} : "
        f"{snapshot['relative_performance']:+.2f} percentage points\n"
    )

    print("Base 100")
    print(
        f"{instrument['ticker']:<5} : "
        f"{instrument_base_100[0]['value']:.2f} -> "
        f"{instrument_base_100[-1]['value']:.2f}"
    )
    print(
        f"{benchmark['ticker']:<5} : "
        f"{benchmark_base_100[0]['value']:.2f} -> "
        f"{benchmark_base_100[-1]['value']:.2f}"
    )


if __name__ == "__main__":
    main()
