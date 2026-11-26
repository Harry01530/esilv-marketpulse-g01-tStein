import json
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent.parent
SAMPLE_FILE = ROOT_DIR / "data" / "sample" / "bloomberg_reference_sample.json"

ACCESS_MODE = "APPROVED_SAMPLE"

# Canonical MarketPulse ticker -> Bloomberg identifier
BLOOMBERG_IDENTIFIERS = {
    "AAPL": "AAPL US Equity",
    "SP500": "SPX Index",
}


def fetch_raw_bloomberg_history(identifier):
    # APPROVED_SAMPLE mode: raw input comes from the approved fixture.
    # No live Bloomberg connection is made here.
    with open(SAMPLE_FILE, encoding="utf-8") as file:
        sample = json.load(file)

    for series in sample["series"]:
        if series["provider_identifier"] == identifier:
            return series

    raise ValueError(f"No Bloomberg-stage series found for {identifier}")


def normalize_bloomberg_history(raw_data, canonical_ticker):
    # Teaching wrapper keys (not Bloomberg field mnemonics),
    # mapped as documented in docs/BLOOMBERG_FIELD_MAPPING.md
    rows = []

    for observation in raw_data["observations"]:
        rows.append({
            "date": observation["observation_date"],
            "ticker": canonical_ticker,
            "open": float(observation["open_value"]),
            "high": float(observation["high_value"]),
            "low": float(observation["low_value"]),
            "close": float(observation["close_value"]),
            "volume": int(observation["volume_value"]),
        })

    return rows


def fetch_bloomberg_prices(canonical_ticker):
    identifier = BLOOMBERG_IDENTIFIERS[canonical_ticker]
    raw_data = fetch_raw_bloomberg_history(identifier)

    if raw_data["canonical_ticker"] != canonical_ticker:
        raise ValueError(
            f"{identifier} does not match canonical ticker {canonical_ticker}"
        )

    rows = normalize_bloomberg_history(raw_data, canonical_ticker)

    if not rows:
        raise ValueError(f"No Bloomberg-stage data for {identifier}")

    return rows