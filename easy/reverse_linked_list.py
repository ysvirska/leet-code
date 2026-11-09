"""206. Reverse Linked List — Easy.
https://leetcode.com/problems/reverse-linked-list/

Reverse a singly linked list and return its new head. Relink the existing
nodes rather than copying their values into a new list.

Examples:
    head = [1, 2, 3, 4, 5] -> [5, 4, 3, 2, 1]
    head = [1, 2] -> [2, 1]
    head = [] -> []

Constraints:
    The list contains between 0 and 5_000 nodes.
    -5_000 <= node.val <= 5_000

Algorithm: save each node's successor, redirect its next pointer to the
already reversed prefix, and advance. Iterate to avoid recursion limits.

Complexity: O(n) time and O(1) extra space.
"""

from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        previous = None
        while head is not None:
            following = head.next
            head.next = previous
            previous = head
            head = following
        return previous
