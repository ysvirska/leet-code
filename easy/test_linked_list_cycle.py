"""Tests for problem 141. Linked List Cycle.
https://leetcode.com/problems/linked-list-cycle/

Detect cycles by node identity, including self-loops, repeated values,
and long lists. The input links must remain unchanged.
"""

import unittest

from easy.linked_list_cycle import ListNode, Solution


class LinkedListCycleTests(unittest.TestCase):
    def test_examples_and_edge_cases(self):
        cases = [
            ([3, 2, 0, -4], 1),
            ([1, 2], 0),
            ([1], -1),
            ([], -1),
            ([0], 0),
            ([1, 1], -1),
            ([1, 1, 1], -1),
            ([-100_000, 100_000], 1),
            ([1, 2, 3, 4, 5], 3),
        ]
        for values, position in cases:
            with self.subTest(values=values, position=position):
                nodes = [ListNode(value) for value in values]
                for current, following in zip(nodes, nodes[1:]):
                    current.next = following
                if position >= 0:
                    nodes[-1].next = nodes[position]
                original_links = [node.next for node in nodes]

                self.assertEqual(
                    Solution().hasCycle(nodes[0] if nodes else None),
                    position >= 0,
                )
                for node, original_next in zip(nodes, original_links):
                    self.assertIs(node.next, original_next)

    def test_maximum_length(self):
        nodes = [ListNode() for _ in range(10_000)]
        for current, following in zip(nodes, nodes[1:]):
            current.next = following
        for position in (-1, 0, 5_000, 9_999):
            with self.subTest(position=position):
                nodes[-1].next = nodes[position] if position >= 0 else None
                self.assertEqual(Solution().hasCycle(nodes[0]), position >= 0)


if __name__ == "__main__":
    unittest.main()
