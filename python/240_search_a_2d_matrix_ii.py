"""
Write an efficient algorithm that searches for a value in an m x n matrix. This
matrix has the following properties:

    Integers in each row are sorted in ascending from left to right.
    Integers in each column are sorted in ascending from top to bottom.

For example,

Consider the following matrix:

    [
      [1,   4,  7, 11, 15],
      [2,   5,  8, 12, 19],
      [3,   6,  9, 16, 22],
      [10, 13, 14, 17, 24],
      [18, 21, 23, 26, 30]
    ]

    Given target = 5, return true.
    
    Given target = 20, return false.
"""
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if matrix is None or matrix == []:
            return False
        x, y = len(matrix) - 1, 0
        while x >= 0 and y < len(matrix[0]):
            if matrix[x][y] == target:
                return True
            elif matrix[x][y] > target:
                x -= 1
            else:
                y += 1
        return False

matrix = [
    [1,   4,  7, 11, 15],
    [2,   5,  8, 12, 19],
    [3,   6,  9, 16, 22],
    [10, 13, 14, 17, 24],
    [18, 21, 23, 26, 30]
]
a = Solution()
print(a.searchMatrix(matrix, 5) == True)
print(a.searchMatrix(matrix, 20) == False)

"""
Notes:
    some fancy solutions:

    http://stackoverflow.com/questions/2457792/given-a-2d-array-sorted-in-increasing-order-from-left-to-right-and-top-to-bottom/2458113#2458113
"""
