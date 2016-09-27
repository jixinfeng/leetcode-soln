"""
Follow up for "Unique Paths":

Now consider if some obstacles are added to the grids. How many unique paths would there be?

An obstacle and empty space is marked as 1 and 0 respectively in the grid.

For example,
There is one obstacle in the middle of a 3x3 grid as illustrated below.

    [
      [0,0,0],
      [0,1,0],
      [0,0,0]
    ]

The total number of unique paths is 2.

Note: m and n will be at most 100.
"""
class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m = len(obstacleGrid[0])
        n = len(obstacleGrid)
        grid = [[0 for j in range(m)] for i in range(n)]
        grid[0][0] = 1
        for i in range(n):
            for j in range(m):
                if obstacleGrid[i][j] == 1:
                    grid[i][j] = 0
                elif i == 0 and j == 0:
                    continue
                elif i == 0:
                    grid[i][j] = grid[i][j - 1]
                elif m == 0:
                    grid[i][j] = grid[i - 1][j]
                else:
                    grid[i][j] = grid[i - 1][j] + grid[i][j - 1]
        return grid[-1][-1]
