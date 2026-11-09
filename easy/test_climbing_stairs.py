"""Tests for problem 70. Climbing Stairs.
https://leetcode.com/problems/climbing-stairs/

Count one-step and two-step routes. Check all allowed inputs against an
independent count of arrangements grouped by the number of two-step moves.
"""

import unittest
from math import comb

from easy.climbing_stairs import Solution


class ClimbingStairsTests(unittest.TestCase):
    def test_examples_and_boundaries(self):
        for steps, expected in [(1, 1), (2, 2), (3, 3), (45, 1_836_311_903)]:
            with self.subTest(steps=steps):
                self.assertEqual(Solution().climbStairs(steps), expected)

    def test_all_inputs_against_combinatorial_count(self):
        for steps in range(1, 46):
            expected = sum(
                comb(steps - doubles, doubles)
                for doubles in range(steps // 2 + 1)
            )
            with self.subTest(steps=steps):
                self.assertEqual(Solution().climbStairs(steps), expected)


if __name__ == "__main__":
    unittest.main()
