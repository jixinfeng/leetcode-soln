"""
Given a string, find the length of the longest substring without repeating
characters.

Examples:

    Given "abcabcbb", the answer is "abc", which the length is 3.

    Given "bbbbb", the answer is "b", with the length of 1.

    Given "pwwkew", the answer is "wke", with the length of 3. Note that the
    answer must be a substring, "pwke" is a subsequence and not a substring.

First try: works but too slow
    def lengthOfLongestSubstring(self, s):
        l=len(s)
        if l==0:
            return str()
        elif l==1:
            return s
        string=list(s)
        maxstring=[]
        skip=0
        for i in range(l):
            if i<skip:
                continue
            window=[string[i]]
            for j in range(i+1,l):
                if string[j] not in window:
                    window.append(string[j])
                else:
                    if len(window)>len(maxstring):
                        maxstring=window
                    skip=window.index(string[j])+1
                    break
        return len(maxstring)

Note:
    Need the length of longest string only, don't need the string
"""
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        l=len(s)
        if l==0:
            return 0
        elif l==1:
            return 1
        lastCharPos={}
        maxStrLen=0
        maxStrStart=0
        for i,ch in enumerate(s):
            if ch in lastCharPos and lastCharPos[ch]>=maxStrStart:
                maxStrStart=lastCharPos[ch]+1
            lastCharPos[ch]=i
            maxStrLen=max(maxStrLen,i-maxStrStart)
        return maxStrLen
