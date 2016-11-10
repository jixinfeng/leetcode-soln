"""
Given a collection of numbers that might contain duplicates, return all possible unique permutations.

For example,
[1,1,2] have the following unique permutations:

    [
      [1,1,2],
      [1,2,1],
      [2,1,1]
    ]
"""
class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        soln = []
        self.dfs(nums, [], soln)
        return soln

    def dfs(self, nums, curr, soln):
        if nums is None or nums == []:
            soln.append(curr)
            return
        for i, num in enumerate(nums):
            if i > 0 and num == nums[i - 1]:
                continue
            self.dfs(nums[:i] + nums[i + 1:], curr + [num], soln)

a = Solution()
print(a.permuteUnique([1,1,2]) == [[1,1,2], [1,2,1], [2,1,1]])
print(a.permuteUnique([1,1]) == [[1,1]])
