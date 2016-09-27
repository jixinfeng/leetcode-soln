"""
Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do
it in place.

Follow up:
    Did you use extra space?

    A straight forward solution using O(mn) space is probably a bad idea.

    A simple improvement uses O(m + n) space, but still not the best solution.

    Could you devise a constant space solution?
"""
class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        row, col = len(matrix), len(matrix[0])
        zRow, zCol = [False] * row, [False] * col

        for i in range(row):
            for j in range(col):
                if matrix[i][j] == 0:
                    zRow[i] = True
                    zCol[j] = True

        for i in range(row):
            if zRow[i]:
                matrix[i] = [0] * col

        for j in range(col):
            if zCol[j]:
                for i in range(row):
                    matrix[i][j] = 0
