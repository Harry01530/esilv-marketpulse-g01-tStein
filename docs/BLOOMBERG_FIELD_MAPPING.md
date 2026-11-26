# Bloomberg Field Mapping

## Access mode

APPROVED_SAMPLE

- **Source:** `data/sample/bloomberg_reference_sample.json`
- **Reference:** `docs/10_BLOOMBERG_INSTRUCTOR_REFERENCE.md`
- **Live connectivity:** not demonstrated

## Market instruments

| Role | Canonical ticker | Bloomberg identifier |
|---|---|---|
| Instrument | AAPL | AAPL US Equity |
| Benchmark | SP500 | SPX Index |

## Field mapping

| MarketPulse field | Source field or mapping | Status / notes |
|---|---|---|
| date | `observation_date` | Teaching wrapper key (`YYYY-MM-DD`), not a Bloomberg LIVE mnemonic |
| ticker | application mapping | Preserves canonical ticker (`AAPL` or `SP500`) |
| open | `open_value` | Teaching wrapper key, not a Bloomberg LIVE mnemonic |
| high | `high_value` | Teaching wrapper key, not a Bloomberg LIVE mnemonic |
| low | `low_value` | Teaching wrapper key, not a Bloomberg LIVE mnemonic |
| close | `close_value` | Teaching wrapper key, not a Bloomberg LIVE mnemonic |
| volume | `volume_value` | Teaching wrapper key, not a Bloomberg LIVE mnemonic |

> **Important contract rule:** `teaching wrapper key != Bloomberg LIVE field mnemonic`. No unverified Bloomberg LIVE field mnemonics were invented, and provider-specific identifiers (`AAPL US Equity`, `SPX Index`) must stop at the provider boundary so `src/analytics.py` continues receiving only `AAPL` and `SP500`.

## TD10 handoff

- **Access mode:** `APPROVED_SAMPLE`
- **Instrument identifier:** `AAPL US Equity` (canonical ticker: `AAPL`)
- **Benchmark identifier:** `SPX Index` (canonical ticker: `SP500`)
- **Date representation:** ISO date string (`YYYY-MM-DD`) mapped from `observation_date`
- **Input structure:** JSON fixture containing instrument and benchmark series with `provider_identifier`, `canonical_ticker`, and daily observation records using teaching wrapper keys
- **Missing fields:** None in `APPROVED_SAMPLE` (all canonical fields are present in the sample fixture; live `blpapi` field names were not observed)
- **Special normalization notes:** Map `AAPL US Equity -> AAPL` and `SPX Index -> SP500` inside `src/providers/bloomberg_provider.py`, cast numeric fields (`open`, `high`, `low`, `close` as `float`, `volume` as `int`), and validate output against the expected reference fixture
- **Expected canonical reference:** `data/sample/bloomberg_reference_expected.json`