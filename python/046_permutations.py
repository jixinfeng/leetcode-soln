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
        if len(nums) <= 1:
            return [nums]
        solns = []
        for i, num in enumerate(nums):
            for tail in self.permute(nums[:i] + nums[i+1:]):
                solns.append([num] + tail)
        return solns


a = Solution()
assert a.permute([1,2,3]) == [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
