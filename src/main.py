from pathlib import Path
import csv
import json

from analytics import (
    align_series,
    calculate_base_100,
    calculate_period_return,
    calculate_relative_performance,
)

# Chemins des fichiers
ROOT_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT_DIR / "data" / "sample"

# Configuration
LOOKBACK_LABEL = "1 month"
INTERVAL_LABEL = "Daily"


def load_instruments():
    with open(DATA_DIR / "instruments.json", encoding="utf-8") as file:
        return json.load(file)


def load_prices():
    with open(DATA_DIR / "prices.csv", encoding="utf-8") as file:
        return list(csv.DictReader(file))


def filter_prices(prices, ticker):
    return [row for row in prices if row["ticker"] == ticker]


def normalize_price_row(row):
    return {
        "date": row["date"],
        "ticker": row["ticker"],
        "open": float(row["open"]),
        "high": float(row["high"]),
        "low": float(row["low"]),
        "close": float(row["close"]),
        "volume": int(row["volume"]),
    }


def main():
    # 1. Chargement des données
    instruments = load_instruments()
    prices = load_prices()

    instrument = instruments["instrument"]
    benchmark = instruments["benchmark"]

    # 2. Normalisation des données
    normalized_prices = [
        normalize_price_row(row)
        for row in prices
    ]

    # 3. Filtrage de l'instrument et du benchmark
    instrument_prices = filter_prices(
        normalized_prices,
        instrument["ticker"],
    )

    benchmark_prices = filter_prices(
        normalized_prices,
        benchmark["ticker"],
    )

    # 4. Alignement des dates communes
    aligned_instrument, aligned_benchmark = align_series(
        instrument_prices,
        benchmark_prices,
    )

    # 5. Calcul des rendements
    instrument_return = calculate_period_return(
        aligned_instrument,
    )

    benchmark_return = calculate_period_return(
        aligned_benchmark,
    )

    relative_performance = calculate_relative_performance(
        instrument_return,
        benchmark_return,
    )

    # 6. Calcul des indices base 100
    instrument_base_100 = calculate_base_100(
        aligned_instrument,
    )

    benchmark_base_100 = calculate_base_100(
        aligned_benchmark,
    )

    # 7. Affichage des résultats
    print("=== MarketPulse ===\n")

    print("Market configuration")
    print(f"Period   : {LOOKBACK_LABEL}")
    print(f"Interval : {INTERVAL_LABEL}")

    print("\nInstrument")
    print(f"{instrument['ticker']} - {instrument['name']}")
    print(f"Observations : {len(aligned_instrument)}")
    print(f"Period return : {instrument_return:.2f}%")

    print("\nBenchmark")
    print(f"{benchmark['ticker']} - {benchmark['name']}")
    print(f"Observations : {len(aligned_benchmark)}")
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