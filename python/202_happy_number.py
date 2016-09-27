"""
Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: Starting with any
positive integer, replace the number by the sum of the squares of its digits,
and repeat the process until the number equals 1 (where it will stay), or it
loops endlessly in a cycle which does not include 1. Those numbers for which
this process ends in 1 are happy numbers.

Example: 19 is a happy number

    1**2 + 9**2 = 82
    8**2 + 2**2 = 68
    6**2 + 8**2 = 100
    1**2 + 0**2 + 0**2 = 1

Credits:
    Special thanks to @mithmatt and @ts for adding this problem and creating all
    test cases.
"""
class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n==1:
            return True
        else:
            path=set()
            path.add(n)
            while True:
                digits=[int(d) for d in str(n)]
                sqsum=sum([d**2 for d in digits])
                if sqsum==1:
                    return True
                elif sqsum in path:
                    return False
                else:
                    path.add(sqsum)
                    n=sqsum
