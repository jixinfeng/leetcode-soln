"""
Given a 2D board containing 'X' and 'O' (the letter O), capture all regions
surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

For example,
    X X X X
    X O O X
    X X O X
    X O X X

After running your function, the board should be:

    X X X X
    X X X X
    X X X X
    X O X X
"""
class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        x = len(board)
        if x <= 2:
            return
        y = len(board[0])
        if y <= 2:
            return
        bfs = collections.deque()
        for i in range(x):
            for j in range(y):
                if i == 0 or i == x - 1 or j == 0 or j == y - 1:
                    if board[i][j] == 'O':
                        bfs.append((i, j))

        while bfs:
            i, j = bfs.popleft()
            if i >= 0 and i < x and j >= 0 and j < y:
                if board[i][j] == 'O':
                    bfs.append((i - 1, j))
                    bfs.append((i + 1, j))
                    bfs.append((i, j - 1))
                    bfs.append((i, j + 1))
                    board[i][j] = 'B'

        for i in range(x):
            for j in range(y):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                if board[i][j] == 'B':
                    board[i][j] = 'O'