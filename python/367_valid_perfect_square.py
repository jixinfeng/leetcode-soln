"""
Given a positive integer num, write a function which returns True if num is a
perfect square else False.

Note: Do not use any built-in library function such as sqrt.

Example 1:

    Input: 16
    Returns: True

Example 2:

    Input: 14
    Returns: False

Credits:
    Special thanks to @elmirap for adding this problem and creating all test
    cases.
"""
class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        for i in range(num + 1):
            power = i ** 2
            if power == num:
                return True
            elif power > num:
                return False

a = Solution()
print(a.isPerfectSquare(16))
print(a.isPerfectSquare(14))
