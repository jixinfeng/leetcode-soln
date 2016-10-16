"""
Implement strStr().

Returns the index of the first occurrence of needle in haystack, or -1 if needle
is not part of haystack.
"""
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if haystack is None or needle is None:
            return -1
        l1 = len(needle)
        l2 = len(haystack)
        if l1 == 0 or haystack == needle:
            return 0
        elif l1 > l2:
            return -1
        for i in range(l2 - l1 + 1):
            if haystack[i:i + l1] == needle:
                return i
        return -1
