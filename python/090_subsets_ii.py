"""
Given a collection of integers that might contain duplicates, nums, return all
possible subsets.

Note: The solution set must not contain duplicate subsets.

For example,
If nums = [1,2,2], a solution is:

    [
      [2],
      [1],
      [1,2,2],
      [2,2],
      [1,2],
      []
    ]
"""
class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.soln = set()
        self.dfs(sorted(nums), [], 0)
        return list(list(subset) for subset in self.soln)

    def dfs(self, nums, subset, loc):
        if loc == len(nums):
            self.soln.add(tuple(subset))
            return
        self.dfs(nums, subset + [nums[loc]], loc + 1)
        self.dfs(nums, subset, loc + 1)

a = Solution()
print(a.subsetsWithDup([1, 2, 2]))
