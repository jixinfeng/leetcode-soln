"""
Write a program to check whether a given number is an ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. For
example, 6, 8 are ugly while 14 is not ugly since it includes another prime
factor 7.

Note that 1 is typically treated as an ugly number.

Credits:
    Special thanks to @jianchao.li.fighter for adding this problem and creating
    all test cases.
"""


class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False

        while not n % 2:
            n //= 2

        while not n % 3:
            n //= 3

        while not n % 5:
            n //= 5

        return n == 1
