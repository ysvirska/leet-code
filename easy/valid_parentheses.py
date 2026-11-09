"""20. Valid Parentheses — Easy.
https://leetcode.com/problems/valid-parentheses/

Determine whether a bracket string is balanced. Each opening bracket
must have a closing bracket of the same type, in the correct order.

Examples:
    s = "()" -> True
    s = "()[]{}" -> True
    s = "(]" -> False
    s = "([])" -> True
    s = "([)]" -> False

Constraints:
    1 <= len(s) <= 10**4
    s contains only the characters ()[]{}.

Algorithm: push opening brackets onto a stack. Each closing bracket must
match the latest unmatched opening bracket. The stack must end empty.

Complexity: O(n) time and O(n) extra space.
"""


class Solution:
    def isValid(self, s: str) -> bool:
        opening_for = {")": "(", "]": "[", "}": "{"}
        stack: list[str] = []

        for bracket in s:
            if bracket in opening_for:
                if not stack or stack.pop() != opening_for[bracket]:
                    return False
            else:
                stack.append(bracket)

        return not stack
