"""Tests for problem 20. Valid Parentheses.
https://leetcode.com/problems/valid-parentheses/

Check matching bracket types and nesting, including input-length limits.
"""

import unittest

from easy.valid_parentheses import Solution


class ValidParenthesesTests(unittest.TestCase):
    def test_examples_and_edge_cases(self):
        cases = [
            ("()", True),
            ("()[]{}", True),
            ("(]", False),
            ("([])", True),
            ("([)]", False),
            ("(", False),
            (")", False),
            (")(", False),
            ("((", False),
            ("{[()]}", True),
            ("{[()]}[", False),
        ]
        for brackets, expected in cases:
            with self.subTest(brackets=brackets):
                self.assertEqual(Solution().isValid(brackets), expected)

    def test_maximum_length(self):
        self.assertTrue(Solution().isValid("(" * 5_000 + ")" * 5_000))
        self.assertTrue(Solution().isValid("[]" * 5_000))
        self.assertFalse(Solution().isValid("(" * 10_000))


if __name__ == "__main__":
    unittest.main()
