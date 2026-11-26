def index_by_date(prices):
    """
    Index observations by date.

    Args:
        prices: List of price observations.

    Returns:
        Dictionary indexed by date.
    """
    return {price["date"]: price for price in prices}


def align_series(asset_prices, benchmark_prices):
    """
    Align two price series using their common dates.

    Args:
        asset_prices: Asset price series.
        benchmark_prices: Benchmark price series.

    Returns:
        Two aligned lists of observations.
    """
    asset_index = index_by_date(asset_prices)
    benchmark_index = index_by_date(benchmark_prices)

    common_dates = sorted(set(asset_index.keys()) & set(benchmark_index.keys()))

    aligned_asset = [asset_index[date] for date in common_dates]
    aligned_benchmark = [benchmark_index[date] for date in common_dates]

    return aligned_asset, aligned_benchmark


def calculate_period_return(prices):
    """
    Calculate the return over a period.

    Args:
        prices: Price series.

    Returns:
        Period return as a decimal.
    """
    if len(prices) < 2:
        return 0.0

    first_price = prices[0]["close"]
    last_price = prices[-1]["close"]

    return round((last_price / first_price) - 1, 10)


def calculate_base_100(prices):
    """
    Normalize prices to a base of 100.

    Args:
        prices: Price series.

    Returns:
        Normalized price series.
    """
    if not prices:
        return []

    first_price = prices[0]["close"]

    result = []

    for price in prices:
        normalized_price = round(price["close"] / first_price * 100, 10)

        result.append({
            **price,
            "close": normalized_price
        })

    return result


def calculate_relative_performance(asset_prices, benchmark_prices):
    """
    Compare the performance of an asset with its benchmark.

    Args:
        asset_prices: Asset price series.
        benchmark_prices: Benchmark price series.

    Returns:
        Relative performance as a decimal.
    """
    aligned_asset, aligned_benchmark = align_series(
        asset_prices,
        benchmark_prices
    )

    asset_return = calculate_period_return(aligned_asset)
    benchmark_return = calculate_period_return(aligned_benchmark)

    return round(asset_return - benchmark_return, 10)