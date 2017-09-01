"""
The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.

![N-Queens Example](https://leetcode.com/static/images/problemset/8-queens.png)

Given an integer n, return all distinct solutions to the n-queens puzzle.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space respectively.

For example,
There exist two distinct solutions to the 4-queens puzzle:

[
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]
"""
class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        if n is None or n <= 0:
            return []
        self.solns = []
        self.dfs(n)
        return [["".join(["." if i != k else "Q" for i in range(len(soln))]) 
                 for j, k in enumerate(soln)] 
                for soln in self.solns]
    
    def dfs(self, n, soln=[]):
        if self.isValid(soln):
            if len(soln) == n:
                self.solns.append(soln)
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
