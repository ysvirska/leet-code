"""Tests for problem 104. Maximum Depth of Binary Tree.
https://leetcode.com/problems/maximum-depth-of-binary-tree/

Find the longest root-to-leaf path in empty, balanced, and deeply skewed
trees, including a tree with the maximum allowed number of nodes.
"""

import unittest

from easy.maximum_depth_of_binary_tree import Solution, TreeNode


class MaximumDepthOfBinaryTreeTests(unittest.TestCase):
    def test_examples_and_edge_cases(self):
        cases = [
            (TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7))), 3),
            (TreeNode(1, right=TreeNode(2)), 2),
            (None, 0),
            (TreeNode(0), 1),
            (TreeNode(-100, TreeNode(100)), 2),
            (TreeNode(0, TreeNode(0, TreeNode(0)), TreeNode(0)), 3),
        ]
        for root, expected in cases:
            with self.subTest(root=root, expected=expected):
                self.assertEqual(Solution().maxDepth(root), expected)

    def test_maximum_depth_without_recursion(self):
        for direction in ("left", "right"):
            with self.subTest(direction=direction):
                root = TreeNode()
                current = root
                for _ in range(9_999):
                    child = TreeNode()
                    setattr(current, direction, child)
                    current = child
                self.assertEqual(Solution().maxDepth(root), 10_000)


if __name__ == "__main__":
    unittest.main()
