"""
There is a fence with n posts, each post can be painted with one of the k
colors.

You have to paint all the posts such that no more than two adjacent fence posts
have the same color.

Return the total number of ways you can paint the fence.

Note:
    n and k are non-negative integers.
"""
class Solution(object):
    def numWays(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        if n==0 or k<=0:
            return 0
        elif n<=2:
            return k**n
        soln=[0 for i in range(n+1)]
        soln[1],soln[2]=k,k*k
        for i in range(3,n+1):
            soln[i]=(k-1)*(soln[i-1]+soln[i-2])
        return soln[-1]

"""
Note:
    Choose the right boundary condition
"""
