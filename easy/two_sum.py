"""1. Two Sum — Easy.
https://leetcode.com/problems/two-sum/

Given a list of integers nums and an integer target, return the indices
of two distinct elements whose sum is target. Exactly one valid pair
exists. The indices may be returned in either order.

Examples:
    nums = [2, 7, 11, 15], target = 9 -> [0, 1]
    nums = [3, 2, 4], target = 6 -> [1, 2]
    nums = [3, 3], target = 6 -> [0, 1]

Constraints:
    2 <= len(nums) <= 10**4
    -10**9 <= nums[i], target <= 10**9
    Exactly one solution exists.

Algorithm: store previously visited numbers and their indices in a
dictionary. For each number, look up target - number before inserting
the current number, so the same element cannot be used twice.

Complexity: O(n) average time and O(n) extra space.
"""


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen: dict[int, int] = {}
        for index, number in enumerate(nums):
            complement = target - number
            if complement in seen:
                return [seen[complement], index]
            seen[number] = index

        raise ValueError("Input must contain a valid pair")
