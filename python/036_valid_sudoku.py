"""
Determine if a Sudoku is valid, according to: 
    [Sudoku Puzzles - The Rules](http://sudoku.com.au/TheRules.aspx).

The Sudoku board could be partially filled, where empty cells are filled with
the character '.'.

![A partially filled sudoku which is valid.]
(http://upload.wikimedia.org/wikipedia/commons/thumb/f/ff/Sudoku-by-L2G-20050714.svg/250px-Sudoku-by-L2G-20050714.svg.png)

Note:
    A valid Sudoku board (partially filled) is not necessarily solvable. Only the
    filled cells need to be validated.
"""
class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        rentries={} #row
        centries={} #column
        bentries={} #box
        for i in range(9):
            rentries[i]=set()
            centries[i]=set()
            bentries[i]=set()
        for i, row in enumerate(board):
            for j, entry in enumerate(row):
                if entry=='.':
                    continue
                box=(i//3)*3+(j//3) #convert i,j to box id
                if entry in rentries[i] or entry in centries[j] or entry in bentries[box]:
                    return False
                else:
                    rentries[i].add(entry)
                    centries[j].add(entry)
                    bentries[box].add(entry)
        return True

a=Solution()
sudoku=[".87654321","2........","3........","4........","5........","6........","7........","8........","9........"]
print(a.isValidSudoku(sudoku))
