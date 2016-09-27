"""
Divide two integers without using multiplication, division and mod operator.

If it is overflow, return MAX_INT.
"""
class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        MAXINT = (2 ** 32 - 1) // 2
        MININT = -(2 ** 32 - 1) // 2
        if divisor == 0:
            return MAXINT
        negative = dividend > 0 and divisor < 0 \
                or dividend < 0 and divisor > 0
        up, down = abs(dividend), abs(divisor)
        soln, shift = 0, 31
        while shift >= 0:
            if up >= down << shift:
                up -= down << shift
                soln += 1 << shift
            shift -= 1
        if soln > MAXINT:
            return MININT if negative else MAXINT
        return -soln if negative else soln

a = Solution()
print(a.divide(1, 1))
print(a.divide(100, 2))
