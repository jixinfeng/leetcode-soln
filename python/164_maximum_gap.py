"""
Given an unsorted array, find the maximum difference between the successive
elements in its sorted form.

Try to solve it in linear time/space.

Return 0 if the array contains less than 2 elements.

You may assume all elements in the array are non-negative integers and fit in
the 32-bit signed integer range.

Credits:
    Special thanks to @porker2008 for adding this problem and creating all test
    cases.
"""
class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums is None or nums == []:
            return 0
        if len(nums) < 2:
            return 0
        nums.sort()
        gap = 0
        for i in range(1, len(nums)):
            gap = max(gap, nums[i] - nums[i - 1])
        return gap

a = Solution()
print(a.maximumGap([4,3,5,6,3,10,6,4,3]))
