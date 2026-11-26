import unittest

from analytics import (
    index_by_date,
    align_series,
    calculate_period_return,
    calculate_base_100,
    calculate_relative_performance,
)


class TestAnalytics(unittest.TestCase):

    def setUp(self):
        self.asset = [
            {"date": "2024-01-01", "close": 100},
            {"date": "2024-01-02", "close": 110},
            {"date": "2024-01-03", "close": 120},
        ]

        self.benchmark = [
            {"date": "2024-01-01", "close": 100},
            {"date": "2024-01-02", "close": 105},
            {"date": "2024-01-03", "close": 110},
        ]

    def test_index_by_date(self):
        result = index_by_date(self.asset)

        self.assertEqual(len(result), 3)
        self.assertEqual(result["2024-01-01"]["close"], 100)

    def test_align_series(self):
        aligned_asset, aligned_benchmark = align_series(
            self.asset,
            self.benchmark
        )

        self.assertEqual(len(aligned_asset), 3)
        self.assertEqual(len(aligned_benchmark), 3)

    def test_calculate_period_return(self):
        result = calculate_period_return(self.asset)

        self.assertAlmostEqual(result, 0.20)

    def test_calculate_base_100(self):
        result = calculate_base_100(self.asset)

        self.assertAlmostEqual(result[0]["close"], 100)
        self.assertAlmostEqual(result[1]["close"], 110)
        self.assertAlmostEqual(result[2]["close"], 120)

    def test_calculate_relative_performance(self):
        result = calculate_relative_performance(
            self.asset,
            self.benchmark
        )

        self.assertAlmostEqual(result, 0.10)


if __name__ == "__main__":
    unittest.main()