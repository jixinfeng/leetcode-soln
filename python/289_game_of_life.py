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


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        for i in range(len(board)):
            for j in range(len(board[0])):
                curr_state = board[i][j]
                neighbor_count = self.count_neighbors(board, i, j)
                flip = False
                if (curr_state and (neighbor_count < 2 or neighbor_count > 3)) or (
                        not curr_state and neighbor_count == 3):
                    flip = True
                board[i][j] = self.encode(curr_state, flip)

        for i in range(len(board)):
            for j in range(len(board[0])):
                board[i][j] = self.decode_next_state(board[i][j])

        return

    def encode(self, curr_state: int, flip: bool) -> int:
        if not flip:
            return curr_state
        else:
            if curr_state == 1:
                # 1 -> 0: -1
                return -1
            else:
                # 0 -> 1: 2
                return 2

    def decode_prev_state(self, curr_state: int) -> int:
        if curr_state in {0, 1}:
            return curr_state
        elif curr_state == -1:
            return 1
        else:
            return 0

    def decode_next_state(self, curr_state: int) -> int:
        return int(curr_state > 0)

    def count_neighbors(self, board: List[List[int]], curr_i: int, curr_j: int) -> int:
        max_i = len(board) - 1
        max_j = len(board[0]) - 1
        neighbor_count = 0
        for d_i in [-1, 0, 1]:
            for d_j in [-1, 0, 1]:
                if d_i == 0 and d_j == 0:
                    continue

                neighbor_i = curr_i + d_i
                neighbor_j = curr_j + d_j
                if neighbor_i < 0 or neighbor_i > max_i or neighbor_j < 0 or neighbor_j > max_j:
                    continue

                neighbor_count += self.decode_prev_state(board[neighbor_i][neighbor_j])

        return neighbor_count


a = Solution()
a.gameOfLife([[1, 1, 1], [1, 0, 1], [1, 1, 1]])
"""
Note:
    state is binary, possible to save next state in higher digit and shift back
"""
