"""Tests for problem 206. Reverse Linked List.
https://leetcode.com/problems/reverse-linked-list/

Reverse the original nodes, including empty lists, repeated values, and
a maximum-length list. Check node identity, values, and termination.
"""

import unittest

from easy.reverse_linked_list import ListNode, Solution


class ReverseLinkedListTests(unittest.TestCase):
    def test_examples_and_edge_cases(self):
        cases = [
            [1, 2, 3, 4, 5],
            [1, 2],
            [],
            [0],
            [1, 1, 1],
            [-5_000, 0, 5_000],
            list(range(-2_500, 2_500)),
        ]
        for values in cases:
            with self.subTest(length=len(values), prefix=values[:5]):
                nodes = [ListNode(value) for value in values]
                for current, following in zip(nodes, nodes[1:]):
                    current.next = following

                head = Solution().reverseList(nodes[0] if nodes else None)
                for node, value in zip(reversed(nodes), reversed(values)):
                    self.assertIs(head, node)
                    self.assertEqual(head.val, value)
                    head = head.next
                self.assertIsNone(head)


if __name__ == "__main__":
    unittest.main()
