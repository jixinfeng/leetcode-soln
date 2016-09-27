"""
Given n pairs of parentheses, write a function to generate all combinations of
well-formed parentheses.

For example, given n = 3, a solution set is:

    [
      "((()))",
      "(()())",
      "(())()",
      "()(())",
      "()()()"
    ]
"""
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        self.soln = []
        if n == 0:
            return self.soln
        self.dfs(n, n, '')
        return self.soln

    def dfs(self, left, right, s):
        if left == 0 and right == 0:
            self.soln.append(s)
        if left > 0:
            self.dfs(left - 1, right, s + '(')
        if left < right:
            self.dfs(left, right - 1, s+ ')')

a = Solution()
print(a.generateParenthesis(3))
