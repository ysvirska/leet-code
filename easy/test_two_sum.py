"""Tests for problem 1. Two Sum.
https://leetcode.com/problems/two-sum/

Find the indices of two distinct elements whose sum is target.
Cover examples, duplicates, zeros, negative numbers, and constraint limits.
"""

import unittest

from easy.two_sum import Solution


class TwoSumTests(unittest.TestCase):
    def test_examples_and_edge_cases(self):
        cases = [
            ([2, 7, 11, 15], 9, [0, 1]),
            ([3, 2, 4], 6, [1, 2]),
            ([3, 3], 6, [0, 1]),
            ([1, 2], 3, [0, 1]),
            ([0, 4, 3, 0], 0, [0, 3]),
            ([-3, 4, 3, 90], 0, [0, 2]),
            ([-1, -2, -3, -4, -5], -8, [2, 4]),
            ([3, 2, 3], 6, [0, 2]),
            ([-10**9, 0, 10**9], 0, [0, 2]),
            ([0, 10**9], 10**9, [0, 1]),
            ([-10**9, 0], -10**9, [0, 1]),
            (list(range(10_000)), 19_997, [9_998, 9_999]),
        ]
        for nums, target, expected in cases:
            with self.subTest(length=len(nums), target=target, expected=expected):
                result = Solution().twoSum(nums, target)
                self.assertEqual(len(result), 2)
                self.assertCountEqual(result, expected)
                self.assertNotEqual(result[0], result[1])
                self.assertEqual(nums[result[0]] + nums[result[1]], target)


if __name__ == "__main__":
    unittest.main()
