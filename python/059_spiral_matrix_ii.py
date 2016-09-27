"""
Given an integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

For example,
Given n = 3,

You should return the following matrix:
    [
      [ 1, 2, 3 ],
      [ 8, 9, 4 ],
      [ 7, 6, 5 ]
    ]
"""
class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        if n == 0:
            return []
        matrix = [[0 for i in range(n)] for j in range(n)]
        x, y = 0, 0
        l, r, u, d = 0, n - 1, 0, n - 1
        direction = 'r'
        matrix[x][y] = 1
        entry = 1
        while entry < n ** 2:
            if direction == 'r':
                while y < r:
                    y += 1
                    entry += 1
                    matrix[x][y] = entry
                direction = 'd'
                u += 1
            elif direction == 'd':
                while x < d:
                    x += 1
                    entry += 1
                    matrix[x][y] = entry
                direction = 'l'
                r -= 1
            elif direction == 'l':
                while y > l:
                    y -= 1
                    entry += 1
                    matrix[x][y] = entry
                direction = 'u'
                d -= 1
            elif direction == 'u':
                while x > u:
                    x -= 1
                    entry += 1
                    matrix[x][y] = entry
                direction = 'r'
                l += 1
        return matrix

a = Solution()
matrix = [
    [1, 2, 3],
    [8, 9, 4],
    [7, 6, 5]
]
print(a.generateMatrix(3) == matrix)
