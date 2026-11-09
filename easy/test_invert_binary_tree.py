"""Tests for problem 226. Invert Binary Tree.
https://leetcode.com/problems/invert-binary-tree/

Mirror tree structure while retaining node identities. Cover examples,
empty and sparse trees, repeated values, and the maximum node count.
"""

import unittest
from collections import deque

from easy.invert_binary_tree import Solution, TreeNode


def build_tree(values):
    if not values:
        return None, []
    root = TreeNode(values[0])
    nodes = [root]
    pending = deque([root])
    remaining = iter(values[1:])
    while pending:
        node = pending.popleft()
        for side in ("left", "right"):
            value = next(remaining, None)
            if value is not None:
                child = TreeNode(value)
                setattr(node, side, child)
                nodes.append(child)
                pending.append(child)
    return root, nodes


class InvertBinaryTreeTests(unittest.TestCase):
    def test_examples_and_edge_cases(self):
        cases = [
            ([4, 2, 7, 1, 3, 6, 9], [4, 7, 2, 9, 6, 3, 1]),
            ([2, 1, 3], [2, 3, 1]),
            ([], []),
            ([0], [0]),
            ([1, 2, None, 3], [1, None, 2, None, 3]),
            ([0, None, -100, 100], [0, -100, None, None, 100]),
            ([1, 1, 1, 1, None, None, 1], [1, 1, 1, 1, None, None, 1]),
        ]
        for values, expected in cases:
            with self.subTest(values=values):
                root, nodes = build_tree(values)
                original_children = {node: (node.left, node.right) for node in nodes}
                result = Solution().invertTree(root)
                self.assertIs(result, root)
                for node, (left, right) in original_children.items():
                    self.assertIs(node.left, right)
                    self.assertIs(node.right, left)

                actual = []
                visited = set()
                pending = deque([result])
                while pending:
                    node = pending.popleft()
                    if node is None:
                        actual.append(None)
                    else:
                        self.assertNotIn(node, visited)
                        visited.add(node)
                        actual.append(node.val)
                        pending.extend((node.left, node.right))
                while actual and actual[-1] is None:
                    actual.pop()
                self.assertEqual(actual, expected)
                self.assertEqual(visited, set(nodes))

    def test_maximum_size_skewed_tree(self):
        nodes = [TreeNode(value) for value in range(100)]
        for node, child in zip(nodes, nodes[1:]):
            node.right = child
        current = Solution().invertTree(nodes[0])
        for node in nodes:
            self.assertIs(current, node)
            self.assertIsNone(current.right)
            current = current.left
        self.assertIsNone(current)


if __name__ == "__main__":
    unittest.main()
