"""
Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

For "(()", the longest valid parentheses substring is "()", which has length = 2.

Another example is ")()())", where the longest valid parentheses substring is "()()", which has length = 4.
"""

class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        soln = 0
        if s is None or s == "":
            return soln
        dp = [0 for i in range(len(s))]
        for i in range(1, len(s)):
            if s[i] == ")" and s[i - 1] == "(":
                dp[i] = dp[max(i - 2, 0)] + 2
            elif s[i] == ")" and s[i - 1] == ")":
                if s[i - dp[i - 1] - 1] == "(":
                    dp[i] = dp[i - 1] + dp[i - dp[i - 1] - 2] + 2
            soln = max(soln, dp[i])
        return soln

a = Solution()
assert a.longestValidParentheses("(()") == 2
assert a.longestValidParentheses(")()())") == 4
