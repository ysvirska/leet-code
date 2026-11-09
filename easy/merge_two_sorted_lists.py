"""21. Merge Two Sorted Lists — Easy.
https://leetcode.com/problems/merge-two-sorted-lists/

Merge two sorted singly linked lists by relinking their existing nodes.
Return the head of the merged list in non-decreasing order.

Examples:
    list1 = [1, 2, 4], list2 = [1, 3, 4] -> [1, 1, 2, 3, 4, 4]
    list1 = [], list2 = [] -> []
    list1 = [], list2 = [0] -> [0]

Constraints:
    Each list has between 0 and 50 nodes.
    -100 <= node.val <= 100
    Both input lists are sorted in non-decreasing order.

Algorithm: append the smaller current node to a dummy-headed list, then
attach the remaining suffix once either input is exhausted.

Complexity: O(m + n) time and O(1) extra space.
"""

from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy

        while list1 is not None and list2 is not None:
            if list1.val <= list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        tail.next = list1 if list1 is not None else list2
        return dummy.next
