"""283. Move Zeroes — Easy.
https://leetcode.com/problems/move-zeroes/

Move all zeros to the end of an integer list in place, preserving the
relative order of its nonzero values. Do not return a replacement list.

Examples:
    nums = [0, 1, 0, 3, 12] -> [1, 3, 12, 0, 0]
    nums = [0] -> [0]

Constraints:
    1 <= len(nums) <= 10**4
    -2**31 <= nums[i] <= 2**31 - 1

Algorithm: scan with a read index and track the next nonzero destination.
Swap each nonzero value into that position. Skip swaps when the indices
are equal to avoid unnecessary writes to an already compact prefix.

Complexity: O(n) time and O(1) extra space.
"""


class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        write = 0
        for read in range(len(nums)):
            if nums[read] != 0:
                if read != write:
                    nums[write], nums[read] = nums[read], nums[write]
                write += 1
