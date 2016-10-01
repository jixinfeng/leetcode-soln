"""
Given a string, find the length of the longest substring without repeating
characters.

Examples:

    Given "abcabcbb", the answer is "abc", which the length is 3.

    Given "bbbbb", the answer is "b", with the length of 1.

    Given "pwwkew", the answer is "wke", with the length of 3. Note that the
    answer must be a substring, "pwke" is a subsequence and not a substring.

Hint:
    Need the length of longest string only, don't need the string
"""
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = len(s)
        if l < 2:
            return l
        lastCharPos = {}
        maxStrLen = 0
        maxStrStart = 0
        for i, ch in enumerate(s):
            if ch in lastCharPos and lastCharPos[ch] >= maxStrStart:
                maxStrStart = lastCharPos[ch] + 1
            lastCharPos[ch] = i
            maxStrLen = max(maxStrLen, i - maxStrStart + 1)
        return maxStrLen
