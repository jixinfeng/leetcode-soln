"""
Given a matrix of m x n elements (m rows, n columns), return all elements of the
matrix in spiral order.

For example,
Given the following matrix:

    [
      [ 1, 2, 3 ],
      [ 4, 5, 6 ],
      [ 7, 8, 9 ]
    ]

You should return [1,2,3,6,9,8,7,4,5].
"""
class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if matrix is None or matrix == []:
            return []
        row, col = len(matrix), len(matrix[0])
        u, d, l, r = 0, row - 1, 0, col - 1
        x, y  = 0, 0
        direction = 'r'
        soln = [matrix[0][0]]
        while len(soln) < row * col:
            if direction == 'r':
                while y < r:
                    y += 1
                    soln.append(matrix[x][y])
                direction = 'd'
                u += 1
            elif direction == 'd':
                while x < d:
                    x += 1
                    soln.append(matrix[x][y])
                direction = 'l'
                r -= 1
            elif direction == 'l':
                while y > l:
                    y -= 1
                    soln.append(matrix[x][y])
                direction = 'u'
                d -= 1
            elif direction == 'u':
                while x > u:
                    x -= 1
                    soln.append(matrix[x][y])
                direction = 'r'
                l += 1
        return soln

a = Solution()
print(a.spiralOrder([]) == [])
print(a.spiralOrder([[2,3]]) == [2,3])
print(a.spiralOrder([[1,2,3],[4,5,6],[7,8,9]]) == [1,2,3,6,9,8,7,4,5])
