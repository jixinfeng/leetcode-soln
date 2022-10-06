"""
There is a fence with n posts, each post can be painted with one of the k
colors.

You have to paint all the posts such that no more than two adjacent fence posts
have the same color.

Return the total number of ways you can paint the fence.

Note:
    n and k are non-negative integers.
"""


class Solution:
    def numWays(self, n: int, k: int) -> int:
        if n == 0:
            return 0
        if n <= 2:
            return k ** n

        dp = [0] * (n + 1)
        dp[1] = k
        dp[2] = k ** 2
        for i in range(3, n + 1):
            dp[i] = (k - 1) * (dp[i - 1] + dp[i - 2])

        return dp[-1]


"""
Note:
    Choose the right boundary condition
"""
