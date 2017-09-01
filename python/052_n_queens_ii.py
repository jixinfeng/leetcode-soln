"""
Follow up for N-Queens problem.

Now, instead outputting board configurations, return the total number of
distinct solutions.

![N-Queens Example](https://leetcode.com/static/images/problemset/8-queens.png)
"""
class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n is None or n <= 0:
            return []
        self.solns = 0
        self.dfs(n)
        return self.solns
        
    def dfs(self, n, soln=[]):
        if self.isValid(soln):
            if len(soln) == n:
                self.solns += 1
            else:
                for i in range(n):
                    self.dfs(n, soln + [i])
            
            return
        else:
            return
    
    def isValid(self, soln):
        if soln == [] or len(soln) == 1:
            return True
        elif soln[-1] in soln[:-1]:
            return False
        else:
            for i in range(len(soln) - 1):
                if abs(soln[-1] - soln[i]) == len(soln) - 1 - i:
                    return False
        return True
