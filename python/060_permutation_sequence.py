"""
The set [1,2,3,…,n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order,
We get the following sequence (ie, for n = 3):

    "123"
    "132"
    "213"
    "231"
    "312"
    "321"

Given n and k, return the kth permutation sequence.

Note: Given n will be between 1 and 9 inclusive.
"""
class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        soln = [str(i + 1) for i in range(n)]
        k %= math.factorial(n)
        k -= 1
        if k == 0:
            return "".join(soln)
        elif k < 0:
            return "".join(soln)[::-1]
        for i in range(n - 1):
            if k == 0:
                break
            step = math.factorial(n - i - 1)
            if k < step:
                continue
            else:
                j, k = divmod(k, step)
                soln[i], soln[i + j] = soln[i + j], soln[i]
                soln[i + 1:] = sorted(soln[i + 1:])
        return "".join(soln)
        
import math
a = Solution()
print(a.getPermutation(3, 1) == "123")
print(a.getPermutation(3, 2) == "132")
print(a.getPermutation(3, 3) == "213")
print(a.getPermutation(3, 4) == "231")
print(a.getPermutation(3, 5) == "312")
print(a.getPermutation(3, 6) == "321")
print(a.getPermutation(5, 100) == "51342")
print(a.getPermutation(2, 2) == "21")
