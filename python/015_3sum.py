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
        soln = []
        length = len(nums)
        for i in range(length - 2):
            if i and nums[i] == nums[i - 1]:
                continue
            target = -1 * nums[i]
            j, k= i + 1, length - 1
            while j < k:
                if nums[j] + nums[k] == target:
                    soln.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                    while nums[j] == nums[j - 1] and j < k:
                        j += 1
                    while nums[k] == nums[k + 1] and j < k:
                        k -= 1
                elif nums[j] + nums[k] < target:
                    j += 1
                    while nums[j] == nums[j - 1] and j < k:
                        j += 1
                elif nums[j] + nums[k] > target:
                    k -= 1
                    while nums[k] == nums[k + 1] and j < k:
                        k -= 1
        return soln



a = Solution()
print(a.threeSum([-1,0,1,2,-1,4]))
