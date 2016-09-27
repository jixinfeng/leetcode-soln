"""
Given an array S of n integers, are there elements a, b, c, and d in S such that
a + b + c + d = target? Find all unique quadruplets in the array which gives the
sum of target.

Note: The solution set must not contain duplicate quadruplets.

For example, given array S = [1, 0, -1, 0, -2, 2], and target = 0.

A solution set is:
    [
      [-1,  0, 0, 1],
      [-2, -1, 1, 2],
      [-2,  0, 0, 2]
    ]
"""
class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if nums is None:
            return []
        length = len(nums)
        solns = set()
        if length < 4:
            return []
        nums.sort()
        twoSums = {}
        for i in range(length):
            for j in range(i + 1, length):
                twoSum = nums[i] + nums[j]
                if twoSum in twoSums:
                    twoSums[twoSum].append([i, j])
                else:
                    twoSums[twoSum] = [[i, j]]
        for k in range(length):
            for l in range(k + 1, length):
                diff = target - nums[k] - nums[l]
                if diff in twoSums:
                    for ij in twoSums[diff]:
                        if ij[0] > l:
                            solns.add(tuple([nums[k], nums[l]] + 
                                            [nums[ij[0]], nums[ij[1]]]))
        return [list(soln) for soln in solns]

a = Solution()
print(a.fourSum([1,0,-1,0,-2,2],0))
print(a.fourSum([1,-2,-5,-4,-3,3,3,5], -11))
