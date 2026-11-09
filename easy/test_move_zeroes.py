"""Tests for problem 283. Move Zeroes.
https://leetcode.com/problems/move-zeroes/

Move zeros to the end in place while keeping nonzero values in order.
Check examples, integer limits, maximum length, and exhaustive short lists.
"""

import unittest
from itertools import product

from easy.move_zeroes import Solution


class MoveZeroesTests(unittest.TestCase):
    def test_examples_and_edge_cases(self):
        cases = [
            ([0, 1, 0, 3, 12], [1, 3, 12, 0, 0]),
            ([0], [0]),
            ([1], [1]),
            ([0, 0, 0], [0, 0, 0]),
            ([1, 2, 3], [1, 2, 3]),
            ([0, 0, 1], [1, 0, 0]),
            ([1, 0, 0], [1, 0, 0]),
            ([0, -1, 0, -1, 2], [-1, -1, 2, 0, 0]),
            ([0, -2**31, 2**31 - 1, 0], [-2**31, 2**31 - 1, 0, 0]),
        ]
        for values, expected in cases:
            with self.subTest(values=values):
                nums = values.copy()
                self.assertIsNone(Solution().moveZeroes(nums))
                self.assertEqual(nums, expected)

    def test_maximum_length(self):
        nums = [0, 1] * 5_000
        self.assertIsNone(Solution().moveZeroes(nums))
        self.assertEqual(nums, [1] * 5_000 + [0] * 5_000)

    def test_small_inputs_against_stable_partition(self):
        for length in range(1, 7):
            for values in product((-1, 0, 1), repeat=length):
                nums = list(values)
                expected = [value for value in values if value != 0]
                expected += [0] * values.count(0)
                with self.subTest(values=values):
                    self.assertIsNone(Solution().moveZeroes(nums))
                    self.assertEqual(nums, expected)


if __name__ == "__main__":
    unittest.main()
