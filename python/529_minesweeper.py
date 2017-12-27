"""
Let's play the minesweeper game (Wikipedia, online game)!

You are given a 2D char matrix representing the game board. 'M' represents an
unrevealed mine, 'E' represents an unrevealed empty square, 'B' represents a
revealed blank square that has no adjacent (above, below, left, right, and all 4
diagonals) mines, digit ('1' to '8') represents how many mines are adjacent to
this revealed square, and finally 'X' represents a revealed mine.

Now given the next click position (row and column indices) among all the
unrevealed squares ('M' or 'E'), return the board after revealing this position
according to the following rules:

If a mine ('M') is revealed, then the game is over - change it to 'X'.

If an empty square ('E') with no adjacent mines is revealed, then change it to
revealed blank ('B') and all of its adjacent unrevealed squares should be
revealed recursively.

If an empty square ('E') with at least one adjacent mine is revealed, then
change it to a digit ('1' to '8') representing the number of adjacent mines.

Return the board when no more squares will be revealed.

Example 1:

Input: 

[['E', 'E', 'E', 'E', 'E'],
 ['E', 'E', 'M', 'E', 'E'],
 ['E', 'E', 'E', 'E', 'E'],
 ['E', 'E', 'E', 'E', 'E']]

Click : [3,0]

Output: 

[['B', '1', 'E', '1', 'B'],
 ['B', '1', 'M', '1', 'B'],
 ['B', '1', '1', '1', 'B'],
 ['B', 'B', 'B', 'B', 'B']]

Example 2:
Input: 

[['B', '1', 'E', '1', 'B'],
 ['B', '1', 'M', '1', 'B'],
 ['B', '1', '1', '1', 'B'],
 ['B', 'B', 'B', 'B', 'B']]

Click : [1,2]

Output: 

[['B', '1', 'E', '1', 'B'],
 ['B', '1', 'X', '1', 'B'],
 ['B', '1', '1', '1', 'B'],
 ['B', 'B', 'B', 'B', 'B']]

Note:

The range of the input matrix's height and width is [1,50].

The click position will only be an unrevealed square ('M' or 'E'), which also
means the input board contains at least one clickable square.

The input board won't be a stage when game is over (some mines have been
revealed).

For simplicity, not mentioned rules should be ignored in this problem. For
example, you don't need to reveal all the unrevealed mines when the game is
over, consider any cases that you will win the game or flag any squares.
"""
from collections import deque
class Solution(object):
    def updateBoard(self, board, click):
        """
        :type board: List[List[str]]
        :type click: List[int]
        :rtype: List[List[str]]
        """
        if not board:
            return board
        self.board = board
        self.height = len(board)
        self.width = len(board[0])
        x, y = click[0], click[1]
        if x < 0 or y < 0 or x >= self.height or y >= self.width:
            return self.board
        elif self.board[x][y] == 'M':
            self.board[x][y] = 'X'
            return self.board
        else:
            return self.bfs(x, y)

    def bfs(self, x, y):
        q = deque([(x, y)])
        searched = {(x, y)}
        while q:
            curr_x, curr_y = q.popleft()
            round_locs = self.get_locs(curr_x, curr_y)
            num_mines = self.count_mines(round_locs)
            if num_mines:
                self.board[curr_x][curr_y] = str(num_mines)
            else:
                self.board[curr_x][curr_y] = 'B'
                for loc in round_locs:
                    if loc not in searched:
                        q.append(loc)
                        searched.add(loc)
        return self.board

    def count_mines(self, locs):
        return sum([self.board[i][j] == 'M' for i, j in locs])
    
    def get_locs(self, x, y):
        x_coords = []
        y_coords = []
        if x > 0:
            x_coords.append(x - 1)
        if y > 0:
            y_coords.append(y - 1)
        x_coords.append(x)
        y_coords.append(y)
        if x < self.height - 1:
            x_coords.append(x + 1)
        if y < self.width - 1:
            y_coords.append(y + 1)
        return [(i, j) 
                for i in x_coords 
                for j in y_coords 
                if i != x or j != y]

a = Solution()
board = [['E', 'E', 'E', 'E', 'E'],
         ['E', 'E', 'M', 'E', 'E'],
         ['E', 'E', 'E', 'E', 'E'],
         ['E', 'E', 'E', 'E', 'E']]
#click = [3,0]
click = [1,2]
a.updateBoard(board, click)
for row in a.board:
    print(row)

