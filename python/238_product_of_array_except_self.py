"""
Given an array of n integers where n > 1, nums, return an array output such that
output[i] is equal to the product of all the elements of nums except nums[i].

Solve it without division and in O(n).

For example, given [1,2,3,4], return [24,12,8,6].

Follow up:
    Could you solve it with constant space complexity? (Note: The output array
    does not count as extra space for the purpose of space complexity analysis.)
"""


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_prod = [1] * len(nums)
        right_prod = [1] * len(nums)

        for i in range(1, len(nums)):
            left_prod[i] = nums[i - 1] * left_prod[i - 1]

        for j in reversed(range(len(nums) - 1)):
            right_prod[j] = nums[j + 1] * right_prod[j + 1]

        solution = [left_prod[k] * right_prod[k] for k in range(len(nums))]

        return solution


a = Solution()
print(a.productExceptSelf([1, 2, 3, 4]))
