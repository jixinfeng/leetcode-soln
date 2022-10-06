"""
Given an integer, write a function to determine if it is a power of two.

Credits:
    Special thanks to @jianchao.li.fighter for adding this problem and creating
    all test cases.
"""


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        while n > 1:
            n, r = divmod(n, 2)
            if r:
                return False

        return n == 1
