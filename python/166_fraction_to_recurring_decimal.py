"""
Given two integers representing the numerator and denominator of a fraction,
return the fraction in string format.

If the fractional part is repeating, enclose the repeating part in parentheses.

For example,

    Given numerator = 1, denominator = 2, return "0.5".
    Given numerator = 2, denominator = 1, return "2".
    Given numerator = 2, denominator = 3, return "0.(6)".

Hint:

    No scary math, just apply elementary math knowledge. Still remember how to
    perform a long division?

    Try a long division on 4/9, the repeating part is obvious. Now try 4/333. Do
    you see a pattern?

    Be wary of edge cases! List out as many test cases as you can think of and
    test your code thoroughly.

Credits:
    Special thanks to @Shangrila for adding this problem and creating all test
    cases.
"""
class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        if denominator == 0:
            return
        if numerator == 0:
            return "0"
        soln = []
        if numerator * denominator < 0:
            neg = True
            soln.append('-')
        else:
            neg = False
        numerator = abs(numerator)
        denominator = abs(denominator)
        if numerator >= denominator:
            quotient, numerator = divmod(numerator, denominator)
            soln.append(str(quotient))
        else:
            soln.append('0')
        if numerator > 0:
            soln.append('.')
            locs = {}
            loc = 0
            while True:
                numerator *= 10
                quotient, remainder = divmod(numerator, denominator)
                if (quotient, remainder) in locs:
                    divided = False
                    break
                if remainder == 0:
                    soln.append(str(quotient))
                    divided = True
                    break
                numerator = remainder
                soln.append(str(quotient))
                locs[(quotient, remainder)] = loc
                loc += 1
        else:
            divided = True
        if not divided:
            if neg:
                soln.insert(locs[(quotient, remainder)] + 3, '(')
            else:
                soln.insert(locs[(quotient, remainder)] + 2, '(')
            soln.append(')')
        return "".join(soln)
        
assert Solution().fractionToDecimal(2, 1) == "2"
assert Solution().fractionToDecimal(-50, 8) == "-6.25"
assert Solution().fractionToDecimal(1, 2) == "0.5"
assert Solution().fractionToDecimal(2, 3) == "0.(6)"
assert Solution().fractionToDecimal(5, 3) == "1.(6)"
assert Solution().fractionToDecimal(1, 7) == "0.(142857)"
assert Solution().fractionToDecimal(1, 17) == "0.(0588235294117647)"
assert Solution().fractionToDecimal(7, 12) == "0.58(3)"
assert Solution().fractionToDecimal(7, -12) == "-0.58(3)"
assert Solution().fractionToDecimal(4, 333) == "0.(012)"
print("pass")
