"""
Given a collection of distinct numbers, return all possible permutations.

For example,
[1,2,3] have the following permutations:

    [
      [1,2,3],
      [1,3,2],
      [2,1,3],
      [2,3,1],
      [3,1,2],
      [3,2,1]
    ]
"""
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if nums is None or nums == []:
            return []
        if len(nums) == 1:
            return [nums]
        if len(nums) == 2:
            return [nums, list(reversed(nums))]
        solns = []
        for i in range(len(nums)):
            residue = nums[:i] + nums[i + 1:]
            for subSoln in self.permute(residue):
                solns.append([nums[i]] + subSoln)
        return solns

a = Solution()
print(a.permute([1,2,3]))
