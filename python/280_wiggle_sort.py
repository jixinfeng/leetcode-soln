"""
Given an unsorted array nums, reorder it in-place such that nums[0] <= nums[1]
>= nums[2] <= nums[3]....

For example, given nums = [3, 5, 2, 1, 6, 4], one possible answer is [1, 6, 2,
5, 3, 4].
"""


class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        for i in range(1, len(nums) - 1, 2):
            nums[i], nums[i + 1] = nums[i + 1], nums[i]


a = Solution()
a.wiggleSort([3, 5, 2, 1, 6, 4])
