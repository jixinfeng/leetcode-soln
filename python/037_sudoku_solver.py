"""
Write a program to solve a Sudoku puzzle by filling the empty cells.

Empty cells are indicated by the character '.'.

You may assume that there will be only one unique solution.

![A sudoku puzzle...](http://upload.wikimedia.org/wikipedia/commons/thumb/f/ff/Sudoku-by-L2G-20050714.svg/250px-Sudoku-by-L2G-20050714.svg.png)

![...and its solution numbers marked in red.](http://upload.wikimedia.org/wikipedia/commons/thumb/3/31/Sudoku-by-L2G-20050714_solution.svg/250px-Sudoku-by-L2G-20050714_solution.svg.png)
"""
class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        self.dfs(board)
        
    def isValid(self, board, x, y):
        # check col
        for i in range(9):
            if i != x and board[i][y] == board[x][y]:
                return False
        
	# check row
        for j in range(9):
            if j != y and board[x][j] == board[x][y]:
                return False
        
        # check 3x3 box
        for i, j in self.getBox(x, y):
            if i != x and j != y and board[i][j] == board[x][y]:
                return False
        
        return True
    
    def dfs(self, board):
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    for k in '123456789':
                        board[i][j] = k
                        if self.isValid(board, i, j) and self.dfs(board):
                            return True
                        board[i][j] = '.'
                    return False
        return True

    def getSeg(self, n):
        if n < 0 or n >= 9:
            raise ValueError("index should be 0 to 8")
        elif n < 3:
            return [0, 1, 2]
        elif n < 6:
            return [3, 4, 5]
        else:
            return [6, 7, 8]

    def getBox(self, row, col):
        rows = self.getSeg(row)
        cols = self.getSeg(col)
        return [(row, col) for row in rows for col in cols]

sudoku = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."], 
    ["6", ".", ".", "1", "9", "5", ".", ".", "."], 
    [".", "9", "8", ".", ".", ".", ".", "6", "."], 
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"], 
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"], 
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"], 
    [".", "6", ".", ".", ".", ".", "2", "8", "."], 
    [".", ".", ".", "4", "1", "9", ".", ".", "5"], 
    [".", ".", ".", ".", "8", ".", ".", "7", "9"]
]

soln = [
    ["5", "3", "4", "6", "7", "8", "9", "1", "2"], 
    ["6", "7", "2", "1", "9", "5", "3", "4", "8"], 
    ["1", "9", "8", "3", "4", "2", "5", "6", "7"], 
    ["8", "5", "9", "7", "6", "1", "4", "2", "3"], 
    ["4", "2", "6", "8", "5", "3", "7", "9", "1"], 
    ["7", "1", "3", "9", "2", "4", "8", "5", "6"], 
    ["9", "6", "1", "5", "3", "7", "2", "8", "4"], 
    ["2", "8", "7", "4", "1", "9", "6", "3", "5"], 
    ["3", "4", "5", "2", "8", "6", "1", "7", "9"]
]
a = Solution()
a.solveSudoku(sudoku)
assert sudoku == soln

sudoku = [
    [".", ".", "9", "7", "4", "8", ".", ".", "."],
    ["7", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", "2", ".", "1", ".", "9", ".", ".", "."],
    [".", ".", "7", ".", ".", ".", "2", "4", "."],
    [".", "6", "4", ".", "1", ".", "5", "9", "."],
    [".", "9", "8", ".", ".", ".", "3", ".", "."],
    [".", ".", ".", "8", ".", "3", ".", "2", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", "6"], 
    [".", ".", ".", "2", "7", "5", "9", ".", "."]
]

soln = [
    ["5", "1", "9", "7", "4", "8", "6", "3", "2"],
    ["7", "8", "3", "6", "5", "2", "4", "1", "9"],
    ["4", "2", "6", "1", "3", "9", "8", "7", "5"],
    ["3", "5", "7", "9", "8", "6", "2", "4", "1"],
    ["2", "6", "4", "3", "1", "7", "5", "9", "8"],
    ["1", "9", "8", "5", "2", "4", "3", "6", "7"],
    ["9", "7", "5", "8", "6", "3", "1", "2", "4"],
    ["8", "3", "2", "4", "9", "1", "7", "5", "6"],
    ["6", "4", "1", "2", "7", "5", "9", "8", "3"]
]

a.solveSudoku(sudoku)
assert sudoku == soln
