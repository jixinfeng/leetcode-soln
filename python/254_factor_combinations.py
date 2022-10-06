"""
Numbers can be regarded as the product of their factors.

For example, 8 = 2 x 2 x 2 = 2 x 4.
Given an integer n, return all possible combinations of its factors. You may return the answer in any order.

Note that the factors should be in the range [2, n - 1].



Example 1:

Input: n = 1
Output: []
Example 2:

Input: n = 12
Output: [[2,6],[3,4],[2,2,3]]
Example 3:

Input: n = 37
Output: []


Constraints:

1 <= n <= 107
"""


class Solution:
    def getFactors(self, n: int) -> List[List[int]]:
        self.solution = []
        self.find(n, 2, [])
        return self.solution

    def find(self, num, start_factor, comb):
        for i in range(start_factor, int(math.sqrt(num)) + 1):
            if num % i == 0:
                comb.append(i)
                self.solution.append(comb + [num // i])
                self.find(num // i, i, comb)
                comb.pop()
