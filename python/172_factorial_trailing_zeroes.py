"""
Given an integer n, return the number of trailing zeroes in n!.

Note: 
    Your solution should be in logarithmic time complexity.

    Need to cound 5 only.

Credits:
Special thanks to @ts for adding this problem and creating all test cases.
"""
class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        c5=0
        i=1
        while i*5<=n:
            c5+=n//(5**i)
            i+=1
        return c5
