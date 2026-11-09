"""121. Best Time to Buy and Sell Stock — Easy.
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

Given daily stock prices, find the largest profit from buying once and
selling on a later day. Return zero if no profitable transaction exists.

Examples:
    prices = [7, 1, 5, 3, 6, 4] -> 5
    prices = [7, 6, 4, 3, 1] -> 0

Constraints:
    1 <= len(prices) <= 10**5
    0 <= prices[i] <= 10**4

Algorithm: scan prices while tracking the lowest price seen and the best
profit so far. Consider selling at the current price before updating the
minimum purchase price. A single day cannot yield a positive profit.

Complexity: O(n) time and O(1) extra space.
"""


class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        minimum_price = prices[0]
        best_profit = 0

        for price in prices:
            best_profit = max(best_profit, price - minimum_price)
            minimum_price = min(minimum_price, price)

        return best_profit
