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
class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        digits=['0']*32
        binDigits=bin(n)[2:]
        for i in range(len(binDigits)):
            digits[i]=binDigits[-(i+1)]
        return int(''.join(digits),2)

a=Solution()
for i in range(10):
    print(i,bin(i)[2:],a.reverseBits(i))
