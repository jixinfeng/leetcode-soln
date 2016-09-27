"""
You are playing the following Flip Game with your friend: Given a string that
contains only these two characters: + and -, you and your friend take turns to
flip two consecutive "++" into "--". The game ends when a person can no longer
make a move and therefore the other person will be the winner.

Write a function to determine if the starting player can guarantee a win.

For example, given s = "++++", return true. The starting player can guarantee a
win by flipping the middle "++" to become "+--+".

Follow up:
    Derive your algorithm's runtime complexity.
"""
class Solution(object):
    def canWin(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) < 2:
            return False
        self.strings = collections.defaultdict(bool)
        for i in range(len(s) - 1):
            if s[i] == '+' and s[i + 1] == '+':
                oppo = s[0:i] + '--' + s[i + 2:]
                if self.canWin(oppo) == False:
                    return True
        return False

a = Solution()
print(a.canWin('++-++'))
