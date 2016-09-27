"""
Given an integer, write a function to determine if it is a power of three.

Follow up:
Could you do it without using any loop / recursion?

Credits:
Special thanks to @dietpepsi for adding this problem and creating all test cases.
"""
class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n==1:
            return True
        if n<1 or n%3>0:
            return False
        return self.isPowerOfThree(n//3)

"""
one line solution:

def isPowerOfThree(self, n):
    return n>0 and 3**round(math.log(n,3))==n
"""
