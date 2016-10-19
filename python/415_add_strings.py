"""
Given two non-negative numbers num1 and num2 represented as string, return the
sum of num1 and num2.

Note: The length of both num1 and num2 is < 5100.

    Both num1 and num2 contains only digits 0-9.

    Both num1 and num2 does not contain any leading zero.

    You must not use any built-in BigInteger library or convert the inputs to
    integer directly.
"""
class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        num1 = num1[::-1]
        num2 = num2[::-1]
        l1 = len(num1)
        l2 = len(num2)
        soln = []
        carry = 0
        for i in range(max(l1, l2) + 1):
            a = int(num1[i]) if i < l1 else 0
            b = int(num2[i]) if i < l2 else 0
            c = a + b + carry
            soln.append(str(c % 10))
            carry = c // 10
        while len(soln) > 1 and soln[-1] == '0':
            soln.pop()
        return ''.join(soln[::-1])

a = Solution()
print(a.addStrings('0', '0') == '0')
print(a.addStrings('1', '1') == '2')
print(a.addStrings('2', '8') == '10')
print(a.addStrings('1', '9999') == '10000')
