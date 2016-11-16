"""
A message containing letters from A-Z is being encoded to numbers using the
following mapping:

    'A' -> 1
    'B' -> 2
    ...
    'Z' -> 26

Given an encoded message containing digits, determine the total number of ways
to decode it.

For example,
Given encoded message "12", it could be decoded as "AB" (1 2) or "L" (12).

The number of ways decoding "12" is 2.
"""
class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s is None or s == "":
            return 0
        dp = [0] * (len(s) + 1)
        dp[0] = 1
        if s[0] != '0':
            dp[1] = 1
        for i in range(2, len(s) + 1):
            if int(s[i - 2:i]) <= 26 and int(s[i - 2:i]) >= 10:
                dp[i] += dp[i - 2]
            if int(s[i - 1]) != 0:
                dp[i] += dp[i - 1]
        return dp[-1]

a = Solution()
print(a.numDecodings('123') == 3)
print(a.numDecodings('242526891011') == 16)
