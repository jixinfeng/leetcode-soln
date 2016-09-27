"""
The gray code is a binary numeral system where two successive values differ in
only one bit.

Given a non-negative integer n representing the total number of bits in the
code, print the sequence of gray code. A gray code sequence must begin with 0.

For example, given n = 2, return [0,1,3,2]. Its gray code sequence is:

    00 - 0
    01 - 1
    11 - 3
    10 - 2

Note:
    For a given n, a gray code sequence is not uniquely defined.

    For example, [0,2,3,1] is also a valid gray code sequence according to the
    above definition.

    For now, the judge is able to judge based on one instance of gray code
    sequence. Sorry about that.
"""
class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        if n < 0:
            return []
        soln = []
        for i in range(2 ** n):
            soln.append(i ^ (i >> 1)) # ^ is the XOR operator
        return soln       

"""
    def grayCode(self, n):
        if n < 0:
            return []
        elif n == 0:
            return [0]
        for i in range(n):
            if i == 0:
                soln = [0, 1]
            else:
                soln += soln[::-1]
                for j in range(2 ** i, 2 ** (i + 1)):
                    soln[j] += 2 ** i
        return soln
"""
