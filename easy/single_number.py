"""136. Single Number — Easy.
https://leetcode.com/problems/single-number/

Find the only number that appears once in a nonempty integer list.
Every other number appears exactly twice. Use linear time and constant
extra space.

Examples:
    nums = [2, 2, 1] -> 1
    nums = [4, 1, 2, 1, 2] -> 4
    nums = [1] -> 1

Constraints:
    1 <= len(nums) <= 3 * 10**4
    -3 * 10**4 <= nums[i] <= 3 * 10**4
    Exactly one number occurs once; all others occur twice.

Algorithm: XOR all values. Each equal pair cancels out, leaving the
number that occurs once.

Complexity: O(n) time and O(1) extra space.
"""


class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        result = 0
        for number in nums:
            result ^= number
        return result
