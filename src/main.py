from pathlib import Path
import csv
import json

# modfi artifie pour le TD07
from analytics import (
    align_series,
    calculate_base_100,
    calculate_period_return,
    calculate_relative_performance,
)

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
# modfi artifie pour le TD03
DATA_DIR = Path("data/sample")

# These starter values mirror config/settings.yml.
# settings.yml is a human-readable configuration contract in the CORE.
# Parsing YAML is optional and is not required by the 18-hour lab sequence.
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

def get_first_date(prices):
    return prices[0]["date"]

def get_last_date(prices):
    return prices[-1]["date"]


def get_first_close(prices):
    first_row = prices[0]
    return float(first_row["close"])


def get_last_close(prices):
    last_row = prices[-1]
    return float(last_row["close"])


def display_market_summary(asset, prices, show_currency=True):
    print(f"{asset['ticker']} - {asset['name']}")
    print(f"Observations : {len(prices)}")
    
    # NOUVEAU : Récupération et affichage des dates
    first_date = get_first_date(prices)
    last_date = get_last_date(prices)
    print(f"First date   : {first_date}")
    print(f"Last date    : {last_date}")
    
    # Reste du code inchangé (les prix de clôture)
    first = get_first_close(prices)
    last = get_last_close(prices)
    
    if show_currency:
        print(f"First close  : {first:.2f} {asset['currency']}")
        print(f"Last close   : {last:.2f} {asset['currency']}")
    else:
        print(f"First close  : {first:.2f}")
        print(f"Last close   : {last:.2f}")

def main():
    instruments = load_instruments()
    raw_prices = load_prices()

    # 1. Conversion des prix (str -> float) et volumes (str -> int)
    normalized_prices = [normalize_price_row(row) for row in raw_prices]

    instrument = instruments["instrument"]
    benchmark = instruments["benchmark"]

    # 2. Filtrage
    instrument_prices = filter_prices(normalized_prices, instrument["ticker"])
    benchmark_prices = filter_prices(normalized_prices, benchmark["ticker"])

    # 3. Alignement et calculs via analytics.py
    aligned_instrument, aligned_benchmark = align_series(
        instrument_prices,
        benchmark_prices,
    )

    instrument_return = calculate_period_return(aligned_instrument)
    benchmark_return = calculate_period_return(aligned_benchmark)
    relative_performance = calculate_relative_performance(
        instrument_return,
        benchmark_return,
    )

    instrument_base_100 = calculate_base_100(aligned_instrument)
    benchmark_base_100 = calculate_base_100(aligned_benchmark)

    # 4. Affichage terminal attendu
    print("=== MarketPulse ===\n")

    print("Market configuration")
    print("Period   : 1 month")
    print("Interval : Daily\n")

    print("Instrument")
    print(f"{instrument['ticker']} - {instrument['name']}")
    print(f"Period return : {instrument_return:.2f}%\n")

    print("Benchmark")
    print(f"{benchmark['ticker']} - {benchmark['name']}")
    print(f"Period return : {benchmark_return:.2f}%\n")

    print("Relative performance")
    print(
        f"{instrument['ticker']} vs {benchmark['ticker']} : "
        f"{relative_performance:+.2f} percentage points\n"
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
