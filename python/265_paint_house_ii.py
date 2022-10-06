"""
There are a row of n houses, each house can be painted with one of the k colors.
The cost of painting each house with a certain color is different. You have to
paint all the houses such that no two adjacent houses have the same color.

The cost of painting each house with a certain color is represented by a n x k
cost matrix. For example, costs[0][0] is the cost of painting house 0 with color
0; costs[1][2] is the cost of painting house 1 with color 2, and so on... Find
the minimum cost to paint all houses.

Note:
    All costs are positive integers.

Follow up:
    Could you solve it in O(nk) runtime?
"""


class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        houses = len(costs)
        colors = len(costs[0])
        dp = [[0 for _ in range(colors)] for _ in range(houses)]
        dp[0] = costs[0]
        for i in range(1, houses):
            for c in range(colors):
                dp[i][c] = min([dp[i - 1][j] for j in range(colors) if c != j]) + costs[i][c]

        return min(dp[-1])
