"""
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you
climb to the top?
"""
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<0:
            return 0
        climbComb=[1 for i in range(n)]
        for i in range(2,n+1):
            climbComb[i]=climbComb[i-1]+climbComb[i-2]
        return climbComb[-1]

"""
Solution above has O(n) speed and O(n) space

Space complexity can be reduced to O(1)
    def climbStairs(self, n):
        a = b = 1
        for x in range(2, n + 1):
            a, b = b, a + b
        return b

and both speed and space can be reduced to O(1)
    def climbStairs(self, n):
        sqrt5 = math.sqrt(5)
        Phi = (1 + sqrt5) / 2
        phi = (1 - sqrt5) / 2
        return int((Phi ** (n + 1) - phi ** (n + 1)) / sqrt5)
"""
