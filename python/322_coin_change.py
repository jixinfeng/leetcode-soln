"""
You are given coins of different denominations and a total amount of money
amount. Write a function to compute the fewest number of coins that you need to
make up that amount. If that amount of money cannot be made up by any
combination of the coins, return -1.

Example 1:
    coins = [1, 2, 5], amount = 11
    return 3 (11 = 5 + 5 + 1)

Example 2:
    coins = [2], amount = 3
    return -1.

Note:
    You may assume that you have an infinite number of each kind of coin.

Credits:
    Special thanks to @jianchao.li.fighter for adding this problem and creating
    all test cases.
"""
class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if amount == 0:
            return 0
        if coins == []:
            return -1
        dp = [0] + [-1] * amount
        for i in range(amount):
            if dp[i] < 0:
                continue
            for coin in coins:
                if i + coin > amount:
                    continue
                if dp[i + coin] < 0 or dp[i + coin] > dp[i] + 1:
                    dp[i + coin] = dp[i] + 1
        return dp[-1]

a = Solution()
print(a.coinChange([1,2,5], 11) == 3)
print(a.coinChange([2], 3) == -1)
print(a.coinChange([186,419,83,408], 6249) == 20)
"""
Notes: solved as integer linear programming

https://discuss.leetcode.com/topic/59509/solving-this-as-a-integer-linear-programming

    def coinChange(self, coins, amount):
        if amount == 0:
            return 0
        if coins == []:
            return -1
        import numpy as np
        from cvxopt import matrix
        from cvxopt.glpk import ilp
        c = np.ones(len(coins))
        A = np.array([coins])
        b = np.array([amount])
        G = np.diag(-1 * np.ones(len(coins)))
        h = np.zeros(len(coins))
        intVars = set(range(len(coins)))
        status, isol = ilp(c = matrix(c.astype(float)),
                           G = matrix(G.astype(float)),
                           h = matrix(h.astype(float)),
                           A = matrix(A.astype(float)), 
                           b = matrix(b.astype(float)),
                           I = intVars)
        return int(sum(isol)) if status == 'optimal' else -1
"""
 
