"""
Find the nth digit of the infinite integer sequence 1, 2, 3, 4, 5, 6, 7, 8, 9,
10, 11, ...

Note:
    n is positive and will fit within the range of a 32-bit signed integer 
    (n < 2 ** 31).

Example 1:

    Input:
    3
    
    Output:
    3

Example 2:

    Input:
    11
    
    Output:
    0

Explanation:
    The 11th digit of the sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ... is a
    0, which is part of the number 10.
"""
class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 0:
            return 0
        elif n <= 9:
            return n
        i = 1
        while n - self.totalDigits(i) >= 0:
            n -= self.totalDigits(i)
            i += 1
        curr = 10 ** (i - 1) + ((n - 1) // i)
        n -= (n // i) * i
        return int(str(curr)[n - 1])

    def totalDigits(self, n):
        return (10 ** n - 10 ** (n - 1)) * n

a = Solution()
print(a.findNthDigit(10) == 1)
print(a.findNthDigit(190) == 1)
