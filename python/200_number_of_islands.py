"""
Given a 2d grid map of '1's (land) and '0's (water), count the number of
islands. An island is surrounded by water and is formed by connecting adjacent
lands horizontally or vertically. You may assume all four edges of the grid are
all surrounded by water.

Example 1:

    11110
    11010
    11000
    00000
    Answer: 1

Example 2:

    11000
    11000
    00100
    00011
    Answer: 3

Credits:
    Special thanks to @mithmatt for adding this problem and creating all test cases.
"""
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if grid is None or grid == [] or grid == [[]]:
            return 0
        x, y = len(grid), len(grid[0])
        if x == 1 and y == 1:
            return int(grid[0][0])

        loc = lambda i, j: i * y + j

        n = x * y
        self.idx = list(range(n))
        self.size = [1] * n
        self.parts = n

        ones = 0
        for i in range(x):
            for j in range(y):
                if grid[i][j] == '1':
                    ones += 1
                    if i + 1 < x and grid[i + 1][j] == '1':
                        self.union(loc(i, j), loc(i + 1, j))
                    if j + 1 < y and grid[i][j + 1] == '1':
                        self.union(loc(i, j), loc(i, j + 1))
        zeros = n - ones

        return self.parts - zeros
    
    def root(self, p):
        while p != self.idx[p]:
            self.idx[p] = self.idx[self.idx[p]]
            p = self.idx[p]
        return p

    def union(self, p, q):
        rootp, rootq = self.root(p), self.root(q)
        if rootp == rootq:
            return
        elif self.size[rootp] > self.size[rootq]:
            self.idx[rootp] = rootq
            self.size[rootq] += self.size[rootp]
        else:
            self.idx[rootq] = rootp
            self.size[rootp] += self.size[rootq]
        self.parts -= 1

a = Solution()
grid = [
    '11110',
    '11010',
    '11000',
    '00000',
]
print(a.numIslands(grid))
grid = [
    '11000',
    '11000',
    '00100',
    '00011',
]
print(a.numIslands(grid))
print(a.numIslands(["1","1"]))
