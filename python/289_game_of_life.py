"""
According to the Wikipedia's article: "The Game of Life, also known simply as
Life, is a cellular automaton devised by the British mathematician John Horton
Conway in 1970."

Given a board with m by n cells, each cell has an initial state live (1) or dead
(0). Each cell interacts with its eight neighbors (horizontal, vertical,
diagonal) using the following four rules (taken from the above Wikipedia
article):

    Any live cell with fewer than two live neighbors dies, as if caused by
    under-population.

    Any live cell with two or three live neighbors lives on to the next
    generation.

    Any live cell with more than three live neighbors dies, as if by
    over-population..

    Any dead cell with exactly three live neighbors becomes a live cell, as if
    by reproduction.

Write a function to compute the next state (after one update) of the board given its current state.

Follow up: 

    Could you solve it in-place? Remember that the board needs to be updated at
    the same time: You cannot update some cells first and then use their updated
    values to update other cells.

    In this question, we represent the board using a 2D array. In principle, the
    board is infinite, which would cause problems when the active area
    encroaches the border of the array. How would you address these problems?

Credits:

    Special thanks to @jianchao.li.fighter for adding this problem and creating
    all test cases.
"""
class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        xLen = len(board)
        yLen = len(board[0])
        xLoc = [-1, -1, -1,  0, 0,  1, 1, 1]
        yLoc = [-1,  0,  1, -1, 1, -1, 0, 1]
        for i in range(xLen):
            for j in range(yLen):
                nCount = 0
                for k in range(8):
                    nCount += self.getCurrentStatus(board, i + xLoc[k],
                                                    j + yLoc[k])
                if nCount == 2:
                    board[i][j] += board[i][j] << 1
                if nCount == 3:
                    board[i][j] += 1 << 1
        for i in range(xLen):
            for j in range(yLen):
                board[i][j] = board[i][j] >> 1

    def getCurrentStatus(self, board, i, j):
        x = len(board) - 1
        y = len(board[0]) - 1
        if i < 0 or i > x:
            return 0
        if j < 0 or j > y:
            return 0
        return board[i][j] & 1

a = Solution()
a.gameOfLife([[1, 1, 1], [1, 0, 1], [1, 1, 1]])
"""
Note:
    state is binary, possible to save next state in higher digit and shift back
"""
