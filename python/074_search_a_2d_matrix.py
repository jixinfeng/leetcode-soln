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
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if matrix is None or matrix == []:
            return False
        for row in matrix:
            if target < row[0]:
                return False
            elif target > row[-1]:
                continue
            else:
                left, right = 0, len(row)-1
                while left < right - 1:
                    middle = (left + right) // 2
                    if row[middle] == target:
                        return True
                    elif row[middle] > target:
                        right = middle
                    else:
                        left = middle
                if row[left] == target or row[right] == target:
                    return True
                else:
                    return False

A=[[1,3,5,7],[10,11,16,20],[23,30,34,50]]
a=Solution()
print(a.searchMatrix(A,3))
