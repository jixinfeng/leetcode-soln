"""
Given an integer (signed 32 bits), write a function to check whether it is a
power of 4.

Example:
    Given num = 16, return true. Given num = 5, return false.

    Follow up: Could you solve it without loops/recursion?

Credits:
    Special thanks to @yukuairoy for adding this problem and creating all
    test cases.

Alternative:

    def isPowerOfFour(self, num):
        if num==1:
            return True
        elif num<=0:
            return False
        while not num%4:
            num//=4
            if num==1:
                return True
        return False
"""
class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num==1:
            return True
        elif num<=0:
            return False
        numBinTail=bin(num)[3:]
        if len(numBinTail)%2:
            return False
        for digit in numBinTail:
            if int(digit):
                return False
        return True
