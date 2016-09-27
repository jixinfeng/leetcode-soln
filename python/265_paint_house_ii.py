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
class Solution(object):
    def minCostII(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        if costs is None or costs == []:
            return 0
        houses = len(costs)
        colors = len(costs[0])
        soln = [[0 for j in range(colors)] for i in range(houses)]
        soln[0] = costs[0][:]
        for i in range(1, houses):
            for j in range(colors):
                soln[i][j] = min(soln[i - 1][:j] + soln[i - 1][j + 1:]) + costs[i][j]
        return min(soln[-1])
