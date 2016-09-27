"""
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the
diagram below).

The robot can only move either down or right at any point in time. The robot is
trying to reach the bottom-right corner of the grid (marked 'Finish' in the
diagram below).

How many possible unique paths are there?

![Sample Grid](http://leetcode.com/wp-content/uploads/2014/12/robot_maze.png)
Above is a 3 x 7 grid. How many possible unique paths are there?

Note: m and n will be at most 100.
"""
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m == 0 or n == 0:
            return 0
        grid = [[0 for j in range(m)] for i in range(n)]
        for i in range(n):
            for j in range(m):
                if i == 0 or j == 0:
                    grid[i][j] = 1
                else:
                    grid[i][j] = grid[i - 1][j] + grid[i][j - 1]
        return grid[-1][-1]
