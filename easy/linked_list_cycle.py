"""141. Linked List Cycle — Easy.
https://leetcode.com/problems/linked-list-cycle/

Determine whether following next pointers in a singly linked list can
visit a node again. The position in examples connects the tail to that
node; -1 means no cycle. It is not an argument to the solution method.

Examples:
    head = [3, 2, 0, -4], pos = 1 -> True
    head = [1, 2], pos = 0 -> True
    head = [1], pos = -1 -> False

Constraints:
    The list contains between 0 and 10**4 nodes.
    -10**5 <= node.val <= 10**5
    pos is -1 or a valid node index.

Algorithm: move slow and fast pointers by one and two nodes. They meet
inside a cycle; otherwise, the fast pointer reaches the end.

Complexity: O(n) time and O(1) extra space.
"""

from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = fast = head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                return True
        return False
