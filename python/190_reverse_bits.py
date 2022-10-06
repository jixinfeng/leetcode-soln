"""
Reverse bits of a given 32 bits unsigned integer.

For example, given input 43261596 (represented in binary as
00000010100101000001111010011100), return 964176192 (represented in binary as
00111001011110000010100101000000).

Follow up:
    If this function is called many times, how would you optimize it?

    Related problem: Reverse Integer

Credits:
    Special thanks to @ts for adding this problem and creating all test
    cases.
"""


class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        power = 31
        while n:
            n, bit = divmod(n, 2)
            result += bit * 2 ** power
            power -= 1
        return result


a = Solution()
for i in range(10):
    print(i, bin(i)[2:], a.reverseBits(i))

"""
class Solution:
    def reverseBits(self, n: int) -> int:
        return int(bin(n)[2:].zfill(32)[::-1], base=2)
"""
