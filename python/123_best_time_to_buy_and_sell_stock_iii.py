"""
Say you have an array for which the ith element is the price of a given stock on
day i.

Design an algorithm to find the maximum profit. You may complete at most two
transactions.

Note:
    You may not engage in multiple transactions at the same time (ie, you must
    sell the stock before you buy again).
"""
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if prices is None:
            return 0
        elif len(prices) < 2:
            return 0
        length = len(prices)
        before = [0 for i in range(length)]
        after = [0 for i in range(length)]
        minPrice = prices[0]
        for i in range(1, length):
            minPrice = min(minPrice, prices[i])
            before[i] = max(before[i - 1], prices[i] - minPrice)
        maxPrice = prices[-1]
        for i in reversed(range(length - 1)):
            maxPrice = max(maxPrice, prices[i])
            after[i] = max(after[i + 1], maxPrice - prices[i])
        soln = 0
        for i in range(length):
            soln = max(soln, before[i] + after[i])
        return soln
        
a = Solution()
