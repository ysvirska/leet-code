"""169. Majority Element — Easy.
https://leetcode.com/problems/majority-element/

Return the element that occupies more than half of a nonempty integer
list. Such an element is guaranteed to exist.

Examples:
    nums = [3, 2, 3] -> 3
    nums = [2, 2, 1, 1, 1, 2, 2] -> 2

Constraints:
    1 <= len(nums) <= 5 * 10**4
    -10**9 <= nums[i] <= 10**9
    A strict majority always exists.

Algorithm: Boyer-Moore voting cancels pairs of different values. Replace
the candidate when its balance reaches zero. The guaranteed majority
survives all cancellations, so no verification pass is needed.

Complexity: O(n) time and O(1) extra space.
"""


class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        candidate = nums[0]
        balance = 0
        for number in nums:
            if balance == 0:
                candidate = number
            balance += 1 if number == candidate else -1
        return candidate
