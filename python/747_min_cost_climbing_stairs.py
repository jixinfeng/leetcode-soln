"""
On a staircase, the i-th step has some non-negative cost cost[i] assigned (0
indexed).

Once you pay the cost, you can either climb one or two steps. You need to find
minimum cost to reach the top of the floor, and you can either start from the
step with index 0, or the step with index 1.

Example 1:

Input: cost = [10, 15, 20]

Output: 15

Explanation: Cheapest is start on cost[1], pay that cost and go to the top.

Example 2:

Input: cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]

Output: 6

Explanation: Cheapest is start on cost[0], and only step on 1s, skipping cost[3].

Note:

cost will have a length in the range [2, 1000].
Every cost[i] will be an integer in the range [0, 999].
"""
class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        if not cost:
            return 0
        if len(cost) <= 2:
            return min(cost)
        total_cost = [0] * (len(cost) + 1)
        for i in range(2, len(cost) + 1):
            print(total_cost)
            total_cost[i] = min(total_cost[i - 1] + cost[i - 1], total_cost[i - 2] + cost[i - 2])
        print(total_cost)
        return total_cost[-1]

a = Solution()
assert a.minCostClimbingStairs([1,1,0,0]) == 1
