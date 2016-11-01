"""
Given a set of distinct integers, nums, return all possible subsets.

Note: The solution set must not contain duplicate subsets.

For example,
If nums = [1,2,3], a solution is:

    [
      [3],
      [1],
      [2],
      [1,2,3],
      [1,3],
      [2,3],
      [1,2],
      []
    ]
"""
class Solution(object):
    def dfs(self, nums, subset, loc):
        if loc == len(nums):
            self.soln.append(subset)
            return
        self.dfs(nums, subset + [nums[loc]], loc + 1)
        self.dfs(nums, subset, loc + 1)

    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.soln = []
        self.dfs(sorted(nums), [], 0)
        return self.soln

a=Solution()
print(a.subsets([1]) == [[1], []])
print(a.subsets([1,2,3]) == 
      [[1, 2, 3], [1, 2], [1, 3], [1], [2, 3], [2], [3], []])
