"""
Say you have an array for which the ith element is the price of a given stock on
day i.

Design an algorithm to find the maximum profit. You may complete at most k
transactions.

Note:
    You may not engage in multiple transactions at the same time (ie, you must
    sell the stock before you buy again).

Credits:
    Special thanks to @Freezen for adding this problem and creating all test
    cases.
"""
class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        if prices is None:
            return 0
        elif len(prices) < 2:
            return 0
        elif k >= len(prices) // 2:
            return self.typeii(prices)
        localProfit = [[0 for j in range(k + 1)] for i in range(len(prices))]
        globalProfit = [[0 for j in range(k + 1)] for i in range(len(prices))]
        for i in range(1, len(prices)):
            diff = prices[i] - prices[i - 1]
            for j in range(1, k + 1):
                localProfit[i][j] = max(globalProfit[i - 1][j - 1],
                                        localProfit[i - 1][j] + diff)
                globalProfit[i][j] = max(globalProfit[i - 1][j],
                                        localProfit[i][j])
        return globalProfit[-1][-1]

    def typeii(self, prices):
        soln = 0
        for i in range(1, len(prices)):
            soln += max(0, prices[i] - prices[i - 1])
        return soln

a = Solution()
print(a.maxProfit(2,[3,2,6,5,0,3]))
print(a.maxProfit(2,[3,3,5,0,0,3,1,4]))

"""
Note:
http://liangjiabin.com/blog/2015/04/leetcode-best-time-to-buy-and-sell-stock.html
"""
