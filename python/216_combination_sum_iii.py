"""
Find all possible combinations of k numbers that add up to a number n, given
that only numbers from 1 to 9 can be used and each combination should be a
unique set of numbers.

Example 1:

    Input: k = 3, n = 7
    
    Output:
    
    [[1,2,4]]

Example 2:

    Input: k = 3, n = 9
    
    Output:
    
    [[1,2,6], [1,3,5], [2,3,4]]
Credits:
    Special thanks to @mithmatt for adding this problem and creating all test
    cases.
"""
class Solution(object):
    def dfs(self, k, n, start, depth, soln):
        if depth == k:
            if n == 0:
                self.solns.append(soln)
            else:
                return
        for i in range(start, 10):
            if n < i:
                return
            self.dfs(k, n - i, i + 1, depth + 1, soln + [i])

    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        self.solns = []
        self.dfs(k, n, 1, 0, [])
        return self.solns
        
a = Solution()
print(a.combinationSum3(3, 9))
