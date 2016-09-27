"""
Calculate the sum of two integers a and b, but you are not allowed to use the
operator + and -.

Example:
    Given a = 1 and b = 2, return 3.

Credits:
    Special thanks to @fujiaozhu for adding this problem and creating all
    test cases.
"""
class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        if a == 0:
            return b
        elif b == 0:
            return a
        sumAB = a ^ b
        carry = a & b
        while carry:
            carry = carry << 1
            newSumAB = sumAB ^ carry
            carry = sumAB & carry
            sumAB = newSumAB
        return sumAB

a=Solution()
print(a.getSum(1,65535))
# can not deal with negative number
