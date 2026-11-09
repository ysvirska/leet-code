"""70. Climbing Stairs — Easy.
https://leetcode.com/problems/climbing-stairs/

Count the distinct ways to climb a staircase of n steps when each move
climbs either one or two steps.

Examples:
    n = 2 -> 2
    n = 3 -> 3

Constraints:
    1 <= n <= 45

Algorithm: the number of ways to reach a step is the sum for the previous
two steps. Compute these counts iteratively, keeping only two values.

Complexity: O(n) time and O(1) extra space.
"""


class Solution:
    def climbStairs(self, n: int) -> int:
        previous, current = 1, 1
        for _ in range(1, n):
            previous, current = current, previous + current
        return current
