"""226. Invert Binary Tree — Easy.
https://leetcode.com/problems/invert-binary-tree/

Mirror a binary tree by swapping every node's left and right children.
Return the root. Examples use level-order notation.

Examples:
    root = [4, 2, 7, 1, 3, 6, 9] -> [4, 7, 2, 9, 6, 3, 1]
    root = [2, 1, 3] -> [2, 3, 1]
    root = [] -> []

Constraints:
    The tree contains between 0 and 100 nodes.
    -100 <= node.val <= 100

Algorithm: traverse iteratively with a stack, swapping child pointers at
each node. All original nodes are retained.

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
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None

        stack = [root]
        while stack:
            node = stack.pop()
            node.left, node.right = node.right, node.left
            if node.left is not None:
                stack.append(node.left)
            if node.right is not None:
                stack.append(node.right)

        return root
