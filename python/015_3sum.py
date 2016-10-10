"""
Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note: The solution set must not contain duplicate triplets.

For example, given array S = [-1, 0, 1, 2, -1, -4],

A solution set is:

    [
      [-1, 0, 1],
      [-1, -1, 2]
    ]
"""
class Solution(object):
    def threeSum(self, nums):
        if nums is None or nums == []:
            return []
        if len(nums) < 3:
            return []
        nums.sort()
        solns = []
        l = len(nums)
        for i in range(0, l - 2):
            if i and nums[i] == nums[i - 1]:
                continue
            j, k= i + 1, l - 1
            while j < k:
                test = nums[i] + nums[j] + nums[k]
                if test == 0:
                    soln = [nums[i], nums[j], nums[k]]
                    solns.append(soln)
                    j += 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                    k -= 1
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1
                elif test > 0:
                    k -= 1
                else:
                    j += 1
        return solns

a = Solution()
print(a.threeSum([-1,0,1,2,-1,4]))
