"""
Given a string s, partition s such that every substring of the partition is a
palindrome.

Return the minimum cuts needed for a palindrome partitioning of s.

For example, given s = "aab",
Return 1 since the palindrome partitioning ["aa","b"] could be produced using 1
cut.
"""
class Solution(object):
    def isParlindrome(self, s):
        return s == s[::-1]

    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s is None or s == "":
            return -1
        if s == s[::-1]:
            return 0
        for i in range(len(s)):
            if self.isParlindrome(s[:i]) and self.isParlindrome(s[i:]):
                return 1
        cut = [i for i in range(-1, len(s))]
        for i in range(len(s)):
            r1, r2 = 0, 0
            while i - r1 >= 0 and i + r1 < len(s) \
                  and s[i - r1] == s[i + r1]:
                cut[i + r1 + 1] = min(cut[i + r1 + 1], cut[i - r1] + 1)
                r1 += 1

            while i - r2 >= 0 and i + r2 + 1< len(s) \
                  and s[i - r2] == s[i + r2 + 1]:
                cut[i + r2 + 2] = min(cut[i + r2 + 2], cut[i - r2] + 1)
                r2 += 1
        return cut[-1]

a = Solution()
print(a.minCut("aabcbcbcbcbcbcbcbijijijijijiji"))
