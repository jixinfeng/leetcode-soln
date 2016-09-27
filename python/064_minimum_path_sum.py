"""
Given a m x n grid filled with non-negative numbers, find a path from top left
to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.
"""
class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if grid is None:
            return None
        m = len(grid[0])
        n = len(grid)
        sums = [[0 for j in range(m)] for i in range(n)]
        for i in range(n):
            for j in range(m):
                if i == 0 and j == 0:
                    sums[i][j] = grid[i][j]
                elif i == 0:
                    sums[i][j] = grid[i][j] + sums[i][j - 1]
                elif j == 0:
                    sums[i][j] = grid[i][j] + sums[i - 1][j]
                else:
                    sums[i][j] = grid[i][j] + \
                        min(sums[i - 1][j], sums[i][j - 1])
        return sums[-1][-1]

a = Solution()
print(a.minPathSum([[1,2],[1,1]]))
