"""104. Maximum Depth of Binary Tree — Easy.
https://leetcode.com/problems/maximum-depth-of-binary-tree/

Return the number of nodes on the longest root-to-leaf path in a binary
tree. An empty tree has depth zero. Examples use level-order notation.

Examples:
    root = [3, 9, 20, None, None, 15, 7] -> 3
    root = [1, None, 2] -> 2

Constraints:
    The tree contains between 0 and 10**4 nodes.
    -100 <= node.val <= 100

Algorithm: traverse iteratively with a stack of nodes and their depths,
recording the largest depth. This also handles very deep trees without
exceeding Python's recursion limit.

Complexity: O(n) time and O(h) extra space, where h is the tree height.
"""

from typing import Optional


class TreeNode:
    def __init__(
        self,
        val: int = 0,
        left: Optional["TreeNode"] = None,
        right: Optional["TreeNode"] = None,
    ):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        maximum = 0
        stack = [(root, 1)]
        while stack:
            node, depth = stack.pop()
            maximum = max(maximum, depth)
            if node.left is not None:
                stack.append((node.left, depth + 1))
            if node.right is not None:
                stack.append((node.right, depth + 1))

        return maximum
