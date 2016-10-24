"""
Given a positive integer n, find the least number of perfect square numbers (for
example, 1, 4, 9, 16, ...) which sum to n.

For example, given n = 12, return 3 because 12 = 4 + 4 + 4; given n = 13, return
2 because 13 = 4 + 9.

Credits:
    Special thanks to @jianchao.li.fighter for adding this problem and creating
    all test cases.
"""
class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = collections.defaultdict(int)
        j = 1
        while j ** 2 <= n:
            dp[j ** 2] = 1
            j += 1
        for i in range(1, n + 1):
            j = 1
            while i + j ** 2 <= n:
                if i + j ** 2 not in dp or dp[i] + 1 < dp[i + j ** 2]:
                    dp[i + j ** 2] = dp[i] + 1
                j += 1
        return dp[n]

import collections
a = Solution()
print(a.numSquares(12) == 3)
print(a.numSquares(13) == 2)
print(a.numSquares(9925) == 2)

"""
Fast (O\sqrt(n)) solution based on Lagrange's Four-Square Theorem:
Original C++ code is here:
https://discuss.leetcode.com/topic/49126/simple-math-solution-4ms-in-c-explained-now
    def numSquares(self, n):
        while n % 4 == 0:
            n /= 4
        if n % 8 == 7:
            return 4
        i = 0
        while i ** 2 <= n:
            j = int(math.sqrt(n - i ** 2))
            if i ** 2 + j ** 2 == n:
                return int(i != 0) + int(j != 0)
            i += 1
        return 3
"""

