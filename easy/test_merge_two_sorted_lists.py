"""Tests for problem 21. Merge Two Sorted Lists.
https://leetcode.com/problems/merge-two-sorted-lists/

Merge sorted lists, preserving every original node without introducing
cycles or allocating replacement nodes in the returned list.
"""

import unittest

from easy.merge_two_sorted_lists import ListNode, Solution


class MergeTwoSortedListsTests(unittest.TestCase):
    def test_examples_and_edge_cases(self):
        cases = [
            ([1, 2, 4], [1, 3, 4]),
            ([], []),
            ([], [0]),
            ([0], []),
            ([1], [2]),
            ([2], [1]),
            ([-100, -2, 0], [-100, -1, 100]),
            ([1, 1, 1], [1, 1]),
            (list(range(-25, 0)), list(range(25))),
        ]
        for left, right in cases:
            with self.subTest(left=left, right=right):
                left_nodes = [ListNode(value) for value in left]
                right_nodes = [ListNode(value) for value in right]
                for nodes in (left_nodes, right_nodes):
                    for current, following in zip(nodes, nodes[1:]):
                        current.next = following

                head = Solution().mergeTwoLists(
                    left_nodes[0] if left_nodes else None,
                    right_nodes[0] if right_nodes else None,
                )
                original_nodes = set(left_nodes + right_nodes)
                visited = set()
                for value in sorted(left + right):
                    self.assertIsNotNone(head)
                    self.assertIn(head, original_nodes)
                    self.assertNotIn(head, visited)
                    visited.add(head)
                    self.assertEqual(head.val, value)
                    head = head.next
                self.assertIsNone(head)
                self.assertEqual(visited, original_nodes)


if __name__ == "__main__":
    unittest.main()
