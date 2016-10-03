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
        if s is None or s == []:
            return ""
        l = len(s)
        if l < 2:
            return s
        maxLeft, maxRight = 0, 0
        maxPalSize = 1
        for i in range(l):
            left, right = self.findPalindrome(s, i)
            if right - left > maxRight - maxLeft:
                maxLeft, maxRight = left, right
            if i + 1 < l and s[i] == s[i + 1]:
                left, right = self.findPalindrome(s, i, even = True)
                if right - left > maxRight - maxLeft:
                    maxLeft, maxRight = left, right
        return s[maxLeft:maxRight + 1]


    def findPalindrome(self, s, loc, even = False):
        if even:
            left, right = loc, loc + 1
        else:
            left, right = loc, loc
        lCap = min(left, len(s) - right - 1)
        for i in range(lCap):
            if s[left] == s[right]:
                left -= 1
                right += 1
            else:
                break
        if left < 0 or right >= len(s) or s[left] != s[right]:
            left += 1
            right -= 1
        return left, right

a = Solution()
print(a.longestPalindrome("aba") == "aba")
print(a.longestPalindrome("abbae") == "abba")
print(a.longestPalindrome("abb") == "bb")
