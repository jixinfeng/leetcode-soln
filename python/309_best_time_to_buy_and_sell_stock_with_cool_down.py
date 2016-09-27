"""
Say you have an array for which the ith element is the price of a given stock on
day i.

Design an algorithm to find the maximum profit. You may complete as many
transactions as you like (ie, buy one and sell one share of the stock multiple
times) with the following restrictions:

You may not engage in multiple transactions at the same time (ie, you must
sell the stock before you buy again).
After you sell your stock, you cannot buy stock on next day. (ie, cooldown 1
day)
Example:

    prices = [1, 2, 3, 0, 2]
    maxProfit = 3
    transactions = [buy, sell, cooldown, buy, sell]

Credits:
    Special thanks to @dietpepsi for adding this problem and creating
    all test cases.
"""
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if prices is None or prices == []:
            return 0
        if len(prices) == 1:
            return 0
        length = len(prices)
        buy = [None] * length
        sell = [None] * length
        buy[0], buy[1] = -prices[0], -1 * min(prices[0], prices[1])
        sell[0], sell[1] = 0, max(0, prices[1] - prices[0])
        for i in range(2, length):
            sell[i] = max(sell[i - 1], buy[i - 1] + prices[i])
            buy[i] = max(buy[i - 1], sell[i - 2] - prices[i])
        return sell[-1]

a = Solution()
print(a.maxProfit([1,2,3,0,2]))
print(a.maxProfit([1,2,4]))
