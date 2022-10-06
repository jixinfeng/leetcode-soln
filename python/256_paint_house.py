"""
There are a row of n houses, each house can be painted with one of the three
colors: red, blue or green. The cost of painting each house with a certain color
is different. You have to paint all the houses such that no two adjacent houses
have the same color.

The cost of painting each house with a certain color is represented by a n x 3
cost matrix. For example, costs[0][0] is the cost of painting house 0 with color
red; costs[1][2] is the cost of painting house 1 with color green, and so on...
Find the minimum cost to paint all houses.

Note:
    All costs are positive integers.
"""


class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        houses = len(costs)
        dp = [[0, 0, 0] for _ in range(houses)]
        dp[0] = costs[0]
        for i in range(1, houses):
            for c in range(3):
                dp[i][c] = min([dp[i - 1][j] for j in range(3) if c != j]) + costs[i][c]

        return min(dp[-1])


a = Solution()
a.minCost([[20, 18, 4], [9, 9, 10]])
