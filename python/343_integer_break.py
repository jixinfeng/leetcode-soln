"""
Given a positive integer n, break it into the sum of at least two positive
integers and maximize the product of those integers. Return the maximum product
you can get.

For example, given n = 2, return 1 (2 = 1 + 1); given n = 10, return 36 (10 = 3
+ 3 + 4).

Note: You may assume that n is not less than 2 and not larger than 58.

Hint:

    There is a simple O(n) solution to this problem.

    You may check the breaking results of n ranging from 7 to 10 to discover the
    regularities.
    
Credits:
    Special thanks to @jianchao.li.fighter for adding this problem and creating
    all test cases.
"""
class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 3:
            return n - 1
        solns = [0 for i in range(n + 1)]
        solns[1], solns[2], solns[3] = 1, 2, 3
        for i in range(4, n + 1):
            solns[i] = max(2 * solns[i - 2], 3 * solns[i - 3])
        return solns[-1]

a = Solution()
for i in range(1, 15):
    print(i,a.integerBreak(i))

"""
Note: Solution that doesn't require dp

    def integerBreak(self, n):
        if n == 2:
            return 1
        elif n == 3:
            return 2
        elif n % 3 == 0:
            return 3 ** (n // 3)
        elif n % 3 == 1:
            return 3 ** ((n // 3) - 1) * 4
        else:
            return 3 ** (n // 3) * 2
"""
