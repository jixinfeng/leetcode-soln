"""
You are playing the following Flip Game with your friend: Given a string that
contains only these two characters: + and -, you and your friend take turns to
flip two consecutive "++" into "--". The game ends when a person can no longer
make a move and therefore the other person will be the winner.

Write a function to compute all possible states of the string after one valid
move.

For example, given s = "++++", after one move, it may become one of the
following states:

    [
      "--++",
      "+--+",
      "++--"
    ]

If there is no valid move, return an empty list [].
"""


class Solution(object):
    def generatePossibleNextMoves(self, currentState: str) -> List[str]:
        """
        :type currentState: str
        :rtype: List[str]
        """
        moves = []
        if len(currentState) <= 1:
            return moves
        for i in range(len(currentState) - 1):
            if currentState[i] == '+' and currentState[i + 1] == '+':
                move = list(currentState)
                move[i], move[i + 1] = '-', '-'
                moves.append(''.join(move))
        return moves
