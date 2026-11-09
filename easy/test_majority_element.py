"""Tests for problem 169. Majority Element.
https://leetcode.com/problems/majority-element/

Find the guaranteed strict majority. Cover cancellation-heavy inputs,
value and length limits, and small inputs checked by counting frequencies.
"""

import unittest
from collections import Counter
from itertools import product

from easy.majority_element import Solution


class MajorityElementTests(unittest.TestCase):
    def test_examples_and_edge_cases(self):
        cases = [
            ([3, 2, 3], 3),
            ([2, 2, 1, 1, 1, 2, 2], 2),
            ([0], 0),
            ([1, 1], 1),
            ([-1, -1, 0], -1),
            ([1, 2, 1, 2, 1], 1),
            ([2, 2, 1, 1, 1], 1),
            ([-10**9, 10**9, -10**9], -10**9),
        ]
        for nums, expected in cases:
            with self.subTest(nums=nums):
                self.assertEqual(Solution().majorityElement(nums), expected)

    def test_maximum_length_with_smallest_majority(self):
        nums = [0, 1] * 24_999 + [1, 1]
        self.assertEqual(Solution().majorityElement(nums), 1)

    def test_small_inputs_against_frequency_counts(self):
        for length in range(1, 8):
            for values in product((-1, 0, 1), repeat=length):
                expected, count = Counter(values).most_common(1)[0]
                if count > length // 2:
                    with self.subTest(values=values):
                        self.assertEqual(
                            Solution().majorityElement(list(values)), expected
                        )


if __name__ == "__main__":
    unittest.main()
