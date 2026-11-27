import pytest

from analytics import (
    align_series,
    calculate_base_100,
    calculate_period_return,
    calculate_relative_performance,
    index_by_date,
)


def test_index_by_date():
    prices = [{"date": "2026-09-01", "close": 100}]
    assert index_by_date(prices)["2026-09-01"]["close"] == 100


def test_align_series():
    instrument = [
        {"date": "2026-09-01", "close": 100},
        {"date": "2026-09-02", "close": 110},
    ]
    benchmark = [
        {"date": "2026-09-02", "close": 200},
        {"date": "2026-09-03", "close": 210},
    ]

    a, b = align_series(instrument, benchmark)

    assert len(a) == len(b) == 1
    assert a[0]["date"] == b[0]["date"] == "2026-09-02"


def test_period_return():
    prices = [{"close": 100}, {"close": 110}]
    assert calculate_period_return(prices) == pytest.approx(10)


def test_relative_performance():
    assert calculate_relative_performance(10, 4) == 6


def test_base_100():
    prices = [
        {"date": "2026-09-01", "ticker": "AAPL", "close": 200},
        {"date": "2026-09-02", "ticker": "AAPL", "close": 220},
    ]

    result = calculate_base_100(prices)

    assert result[0]["value"] == pytest.approx(100)
    assert result[1]["value"] == pytest.approx(110)
