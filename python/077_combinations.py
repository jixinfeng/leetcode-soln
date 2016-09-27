"""
Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

For example,
If n = 4 and k = 2, a solution is:

    [
      [2,4],
      [3,4],
      [2,3],
      [1,2],
      [1,3],
      [1,4],
    ]
"""
class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        if n == 0 or k == 0:
            return []
        self.soln = []
        self.findComb([], [i for i in range(1, n + 1)], k)
        return self.soln

    def findComb(self, prefix, candidates, k):
        if len(candidates) < k:
            return
        if k == 1:
            for j in candidates:
                self.soln.append(prefix + [j])
        else:
            for i, j in enumerate(candidates):
                self.findComb(prefix + [j], candidates[i + 1:], k - 1)

a = Solution()
print(a.combine(10, 5))

"""
Note:
    cheat with python built-in iteration tools

    def combine(self, n, k):
        return [comb for comb in itertools.combinations(range(1, n + 1), k)]
"""
