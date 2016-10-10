"""
Given an array S of n integers, find three integers in S such that the sum is
closest to a given number, target. Return the sum of the three integers. You
may assume that each input would have exactly one solution.

For example, given array S = {-1 2 1 -4}, and target = 1.

The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
"""
class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        MAXINT = 2 ** 31 - 1
        if nums is None:
            return MAXINT
        l = len(nums)
        if l < 3:
            return MAXINT
        nums.sort()
        minDiff = MAXINT
        minDiffSum = MAXINT
        for i in range(l - 2):
            if i and nums[i] == nums[i - 1]:
                continue
            j, k = i + 1, l - 1
            while j < k:
                test = nums[i] + nums[j] + nums[k]
                if test == target:
                    return target
                elif test < target:
                    j += 1
                else:
                    k -= 1
                if abs(target - test) < minDiff:
                    minDiff = abs(target - test)
                    minDiffSum = test
        return minDiffSum

a = Solution()
print(a.threeSumClosest([-1,2,1,-4], 1) == 2)
print(a.threeSumClosest([0,1,2], 3) == 3)
