"""
Given two words word1 and word2, find the minimum number of steps required to
convert word1 to word2. (each operation is counted as 1 step.)

You have the following 3 operations permitted on a word:

    a) Insert a character
    b) Delete a character
    c) Replace a character
"""
class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        m = len(word1) + 1
        n = len(word2) + 1
        states = [[0 for j in range(n)] for i in range(m)]
        for j in range(n):
            states[0][j] = j
        for i in range(m):
            states[i][0] = i
        for i in range(1, m):
            for j in range(1, n):
                states[i][j] = min(states[i - 1][j] + 1,
                                   states[i][j - 1] + 1,
                                   states[i - 1][j - 1] +
                                   (0 if word1[i - 1] == word2[j - 1] else 1))
        return states[m - 1][n - 1]

a = Solution()
assert a.minDistance("hello", "holla") == 2
