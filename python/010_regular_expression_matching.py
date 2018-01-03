"""
Implement regular expression matching with support for '.' and '*'.

'.' Matches any single character.
'*' Matches zero or more of the preceding element.

The matching should cover the entire input string (not partial).

The function prototype should be:
bool isMatch(const char *s, const char *p)

Some examples:
    isMatch("aa","a") → false
    isMatch("aa","aa") → true
    isMatch("aaa","aa") → false
    isMatch("aa", "a*") → true
    isMatch("aa", ".*") → true
    isMatch("ab", ".*") → true
    isMatch("aab", "c*a*b") → true
"""
import unittest

class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        dp = [[False for i in range(len(p) + 1)] for j in range(len(s) + 1)]
        dp[0][0] = True
        for j in range(1, len(p) + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 2]
        for i in range(1, len(s) + 1):
            for j in range(1, len(p) + 1):
                if p[j - 1] == '*':
                    dp[i][j] = dp[i][j - 2]
                    if s[i - 1] == p[j - 2] or p[j - 2] == '.':
                        dp[i][j] |= dp[i - 1][j]
                elif p[j - 1] == s[i - 1] or p[j - 1] == '.':
                    dp[i][j] = dp[i - 1][j - 1]

        return dp[-1][-1]

class TestSolution(unittest.TestCase):
    def test_char_only_neq(self):
        self.assertFalse(Solution().isMatch("aa", "a"))

    def test_char_only_eq(self):
        self.assertTrue(Solution().isMatch("aa", "aa"))

    def test_dot_eq(self):
        self.assertTrue(Solution().isMatch("ab", ".*"))

    def test_star_eq(self):
        self.assertTrue(Solution().isMatch("aab", "c*a*b"))

    def test_star_neq(self):
        self.assertFalse(Solution().isMatch("aaa", "ab*a"))

unittest.main()
