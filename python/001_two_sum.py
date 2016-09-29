"""
Given an array of integers, return indices of the two numbers such that they add
up to a specific target.

You may assume that each input would have exactly one solution.

Example:
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

UPDATE (2016/2/13):
The return format had been changed to zero-based indices. Please read the above
updated description carefully.
"""
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        l=len(nums)
        numsLoc = collections.defaultdict(list)
        for i, j in enumerate(nums):
            numsLoc[j].append(i)
        for i in range(l):
            num1 = nums[i]
            num2 = target - num1
            if num2 in numsLoc:
                for j in numsLoc[num2]:
                    if j > i:
                        return [i, j]
                        
import collections
a = Solution()
print(a.twoSum([2, 7, 11, 15], 9) == [0, 1])
print(a.twoSum([3, 2, 4], 6) == [1, 2])
print(a.twoSum([0, 4, 3, 0], 0) == [0, 3])
