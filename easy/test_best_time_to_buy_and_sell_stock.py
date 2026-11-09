"""Tests for problem 121. Best Time to Buy and Sell Stock.
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

Find the best profit from one purchase followed by one sale, or zero.
Cover examples, edge cases, input limits, and exhaustive small inputs.
"""

import unittest
from itertools import product

from easy.best_time_to_buy_and_sell_stock import Solution


class BestTimeToBuyAndSellStockTests(unittest.TestCase):
    def test_examples_and_edge_cases(self):
        cases = [
            ([7, 1, 5, 3, 6, 4], 5),
            ([7, 6, 4, 3, 1], 0),
            ([7], 0),
            ([0], 0),
            ([1, 2], 1),
            ([2, 1], 0),
            ([4, 4, 4], 0),
            ([0, 1, 0, 3], 3),
            ([10_000, 0, 10_000], 10_000),
            ([2, 4, 1], 2),
            ([3, 2, 6, 5, 0, 3], 4),
            ([1, 4, 2, 8], 7),
        ]
        for prices, expected in cases:
            with self.subTest(prices=prices):
                self.assertEqual(Solution().maxProfit(prices), expected)

    def test_maximum_input_length(self):
        cases = [
            ([0] + [10_000] * 99_999, 10_000),
            ([10_000] * 99_999 + [0], 0),
        ]
        for prices, expected in cases:
            with self.subTest(expected=expected):
                self.assertEqual(Solution().maxProfit(prices), expected)

    def test_exhaustive_small_inputs_against_all_transactions(self):
        for length in range(1, 6):
            for values in product(range(3), repeat=length):
                prices = list(values)
                expected = max(
                    (prices[sell] - prices[buy]
                     for buy in range(length)
                     for sell in range(buy + 1, length)),
                    default=0,
                )
                with self.subTest(prices=prices):
                    self.assertEqual(
                        Solution().maxProfit(prices), max(0, expected)
                    )


if __name__ == "__main__":
    unittest.main()
