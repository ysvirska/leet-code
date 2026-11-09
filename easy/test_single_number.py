"""Tests for problem 136. Single Number.
https://leetcode.com/problems/single-number/

Find the unpaired value among pairs, including zero, negative values,
value limits, and the largest valid odd input length.
"""

import unittest

from easy.single_number import Solution


class SingleNumberTests(unittest.TestCase):
    def test_examples_and_edge_cases(self):
        cases = [
            ([2, 2, 1], 1),
            ([4, 1, 2, 1, 2], 4),
            ([1], 1),
            ([0], 0),
            ([0, -1, -1], 0),
            ([-3, 2, 2], -3),
            ([-30_000, 30_000, -30_000], 30_000),
            ([30_000, -30_000, 30_000], -30_000),
        ]
        for nums, expected in cases:
            with self.subTest(nums=nums):
                self.assertEqual(Solution().singleNumber(nums), expected)

    def test_largest_valid_input_length(self):
        pairs = list(range(14_999))
        nums = pairs + [-30_000] + pairs[::-1]
        self.assertEqual(Solution().singleNumber(nums), -30_000)


if __name__ == "__main__":
    unittest.main()
