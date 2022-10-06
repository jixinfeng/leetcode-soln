"""
Write a function that takes an unsigned integer and returns the number of ’1'
bits it has (also known as the Hamming weight).

For example, the 32-bit integer ’11' has binary representation
00000000000000000000000000001011, so the function should return 3.

Credits:
    Special thanks to @ts for adding this problem and creating all test cases.
"""


class Solution:
    def hammingWeight(self, n: int) -> int:
        sum_of_one = 0
        while n:
            n, bit = divmod(n, 2)
            sum_of_one += bit
        return sum_of_one
