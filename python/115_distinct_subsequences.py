"""
Given a string S and a string T, count the number of distinct subsequences of T
in S.

A subsequence of a string is a new string which is formed from the original
string by deleting some (can be none) of the characters without disturbing the
relative positions of the remaining characters. (ie, "ACE" is a subsequence of
"ABCDE" while "AEC" is not).

Here is an example:
    S = "rabbbit", T = "rabbit"

    Return 3.
"""
class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        if s is None or t is None:
            return 0
        elif len(s) == 0 or len(t) == 0:
            return 0
        solns = [[0 for j in range(len(t) + 1)] for i in range(len(s) + 1)]
        solns[0][0] = 1
        for i in range(1, len(s) + 1):
            solns[i][0] = 1
            for j in range(1, len(t) + 1):
                if s[i - 1] == t[j - 1]:
                    solns[i][j] = solns[i - 1][j - 1] + solns[i - 1][j]
                else:
                    solns[i][j] = solns[i - 1][j]
        return solns[-1][-1]

a = Solution()
print(a.numDistinct("rabbbit", "rabbit"))
