"""
Given two numbers represented as strings, return multiplication of the numbers
as a string.

Note:
    The numbers can be arbitrarily large and are non-negative.

    Converting the input string to integer is NOT allowed.

    You should NOT use internal library such as BigInteger.
"""
class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        num1 = num1[::-1]
        num2 = num2[::-1]
        l1 = len(num1)
        l2 = len(num2)
        soln = [0] * (l1 + l2)
        for i in range(l1):
            a = int(num1[i])
            for j in range(l2):
                b = int(num2[j])
                soln[i + j] += a * b
        carry = 0
        for k in range(l1 + l2):
            soln[k] += carry
            carry = soln[k] // 10
            soln[k] = str(soln[k] % 10)
        while len(soln) > 1 and soln[-1] == '0':
            soln.pop()
        return ''.join(soln[::-1])

a = Solution()
print(a.multiply('0', '0') == '0')
print(a.multiply('11', '11') == '121')
print(a.multiply('1111', '1111') == '1234321')
print(a.multiply('111111111', '111111111') == '12345678987654321')
