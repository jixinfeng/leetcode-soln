"""
Given a string S, find the longest palindromic substring in S. You may assume
that the maximum length of S is 1000, and there exists one unique longest
palindromic substring.
"""
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if s is None or s == "":
            return ""
        if len(s) < 2:
            return s

        currLen = 0
        currStr = ""
        for i in range(len(s)):
            if self.isPalindrome(s, i - currLen - 1, i):
                currStr = s[i - currLen - 1 : i + 1]
                currLen += 2
            elif self.isPalindrome(s, i - currLen, i):
                currStr = s[i - currLen : i + 1]
                currLen += 1
        return currStr

    def isPalindrome(self, s, begin, end):
        if begin < 0:
            return False

        while begin < end:
            if s[begin] != s[end]:
                return False
            else:
                begin, end = begin + 1, end - 1

        return True

a = Solution()
assert a.longestPalindrome("aba") == "aba"
assert a.longestPalindrome("abbae") == "abba"
assert a.longestPalindrome("abb") == "bb"
