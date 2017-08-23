"""
Given an unsorted integer array, find the first missing positive integer.

For example,
Given [1,2,0] return 3,
and [3,4,-1,1] return 2.

Your algorithm should run in O(n) time and uses constant space.
"""

class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums is None or nums == []:
            return 1
        i = 0
        n = len(nums)
        while i < n:
            if nums[i] > 0 and nums[i] < n and nums[i] != nums[nums[i] - 1]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
            else:
                i += 1
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        return n + 1


a = Solution()
assert a.firstMissingPositive([1,2,0]) == 3
assert a.firstMissingPositive([3,4,-1,1]) == 2
assert a.firstMissingPositive([2]) == 1
assert a.firstMissingPositive([1,1]) == 2
assert a.firstMissingPositive([1000,-1]) == 1
