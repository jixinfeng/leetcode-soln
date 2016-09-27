"""
Write a program to find the nth super ugly number.

Super ugly numbers are positive numbers whose all prime factors are in the given
prime list primes of size k. For example, [1, 2, 4, 7, 8, 13, 14, 16, 19, 26,
28, 32] is the sequence of the first 12 super ugly numbers given primes = [2, 7,
13, 19] of size 4.

Note:
    (1) 1 is a super ugly number for any given primes.
    (2) The given numbers in primes are in ascending order.
    (3) 0 < k ≤ 100, 0 < n ≤ 106, 0 < primes[i] < 1000.

Credits:
    Special thanks to @dietpepsi for adding this problem and creating all test
    cases.
"""
class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        uList = [1]
        iList = [0] * len(primes)
        for i in range(n - 1):
            cands = [uList[iList[idx]] * primes[idx] for idx in range(len(primes))]
            nextUgly = min(cands)
            for j in range(len(primes)):
                if cands[j] == nextUgly:
                    iList[j] += 1
            uList.append(nextUgly)
        return uList[-1]

import heapq
a = Solution()
primes = [2, 7, 13, 19]
n = 12
ans = [1, 2, 4, 7, 8, 13, 14, 16, 19, 26, 28, 32] 
for i in range(n):
    print(a.nthSuperUglyNumber(i + 1, primes) == ans[i])
