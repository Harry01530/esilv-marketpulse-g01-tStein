\# Bloomberg Field Mapping



\## Access mode



APPROVED\_SAMPLE



\- Source: data/sample/bloomberg\_reference\_sample.json

\- Reference: docs/10\_BLOOMBERG\_INSTRUCTOR\_REFERENCE.md

\- Live connectivity: not demonstrated



The sample is an instructor-approved fallback fixture (`is\_live\_bloomberg\_output: false`).

Its values are illustrative teaching values, not certified Bloomberg observations.



\## Market instruments



| Role | Canonical ticker | Bloomberg identifier |

|---|---|---|

| Instrument | AAPL | AAPL US Equity |

| Benchmark | SP500 | SPX Index |



The Bloomberg identifier is used only at the provider boundary.

analytics.py keeps receiving the canonical tickers AAPL and SP500.



\## Inspected inputs



| Series | provider\_identifier | canonical\_ticker | Observations | Period |

|---|---|---|---|---|

| Instrument | AAPL US Equity | AAPL | 21 | 2026-09-01 to 2026-09-30 |

| Benchmark | SPX Index | SP500 | 21 | 2026-09-01 to 2026-09-30 |



Structure: JSON object with a `series` list; each series has `role`,

`canonical\_ticker`, `provider\_identifier` and a list of `observations`.

No missing values were found in the inspected observations.



\## Field mapping



| MarketPulse field | Source field or mapping | Status / notes |

|---|---|---|

| date | observation\_date | teaching wrapper key, string YYYY-MM-DD |

| ticker | application mapping | from series canonical\_ticker: AAPL or SP500 |

| open | open\_value | teaching wrapper key, convert to float |

| high | high\_value | teaching wrapper key, convert to float |

| low | low\_value | teaching wrapper key, convert to float |

| close | close\_value | teaching wrapper key, convert to float |

| volume | volume\_value | teaching wrapper key, convert to int |



Important: teaching wrapper key != Bloomberg LIVE field mnemonic.

No Bloomberg LIVE field name is claimed in this document.



\## TD10 handoff



\- Access mode: APPROVED\_SAMPLE

\- Instrument identifier: AAPL US Equity -> canonical AAPL

\- Benchmark identifier: SPX Index -> canonical SP500

\- Date representation: string YYYY-MM-DD in observation\_date

\- Input structure: JSON, series list, one entry per instrument, observations list per series

\- Missing fields: none in the approved sample

\- Special normalization notes: ticker must come from canonical\_ticker, never from provider\_identifier; cast prices to float and volume to int

\- Expected canonical reference: data/sample/bloomberg\_reference\_expected.json

