"""
Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where
"adjacent" cells are those horizontally or vertically neighboring. The same
letter cell may not be used more than once.

For example,
Given board =

    [
      ['A','B','C','E'],
      ['S','F','C','S'],
      ['A','D','E','E']
    ]

    word = "ABCCED", -> returns true,
    word = "SEE", -> returns true,
    word = "ABCB", -> returns false.
"""
class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if word == []:
            return True
        if board == []:
            return False
        x = len(board)
        y = len(board[0])
        for i in range(x):
            for j in range(y):
                if board[i][j] == word[0]:
                    tempBoard = board[:]
                    if self.search(tempBoard, word[1:], i, j):
                        return True
        return False

    def search(self, board, word, i, j):
        if not word:
            return True
        x = len(board)
        y = len(board[0])
        removed = board[i][j]
        board[i][j] = '#'
        if i - 1 >= 0 and board[i - 1][j] == word[0]:
            if self.search(board, word[1:], i - 1, j):
                return True
        if i + 1 < x and board[i + 1][j] == word[0]:
            if self.search(board, word[1:], i + 1, j):
                return True
        if j - 1 >= 0 and board[i][j - 1] == word[0]:
            if self.search(board, word[1:], i, j - 1):
                return True
        if j + 1 < y and board[i][j + 1] == word[0]:
            if self.search(board, word[1:], i, j + 1):
                return True
        board[i][j] = removed
        return False

a = Solution()
board = \
    [
      ['A','B','C','E'],
      ['S','F','C','S'],
      ['A','D','E','E']
    ]
print(a.exist(board, "SEE") == True)
print(a.exist(board, "ABCCED") == True)
print(a.exist(board, "ABCB") == False)

board = \
        [
            ['A','B','C','E'],
            ['S','F','E','S'],
            ['A','D','E','E']
        ]
print(a.exist(board,"ABCESEEEFS") == True)
