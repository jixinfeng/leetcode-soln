"""
Given a string which consists of lowercase or uppercase letters, find the length
of the longest palindromes that can be built with those letters.

This is case sensitive, for example "Aa" is not considered a palindrome here.

Note:
    Assume the length of given string will not exceed 1,010.

Example:

Input:
    "abccccdd"

Output:
    7

Explanation:
    One longest palindrome that can be built is "dccaccd", whose length is 7.
"""
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        sCount = collections.Counter(s)
        soln = 0
        single = 0
        for i, j in sCount.items():
            if j % 2 == 0:
                soln += j
            elif j > 2:
                soln += j - 1
                single = 1
            else:
                single = 1
        return soln + single

import collections
a = Solution()
print(a.longestPalindrome("abccccdd") == 7)
