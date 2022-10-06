"""
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
For example,

Consider the following matrix:

    [
      [1,   3,  5,  7],
      [10, 11, 16, 20],
      [23, 30, 34, 50]
    ]

Given target = 3, return true.
"""


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        if not m:
            return False

        n = len(matrix[0])

        left, right = 0, m * n - 1

        while left <= right:
            mid = left + (right - left) // 2
            i, j = divmod(mid, n)
            mid_val = matrix[i][j]

            if mid_val == target:
                return True
            else:
                if target < mid_val:
                    right = mid - 1
                else:
                    left = mid + 1

        return False


A = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]]
a = Solution()
print(a.searchMatrix(A, 3))
