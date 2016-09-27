"""
Given a string s, partition s such that every substring of the partition is a palindrome.

Return all possible palindrome partitioning of s.

For example, given s = "aab",
Return
    [
      ["aa","b"],
      ["a","a","b"]
    ]
"""
class Solution(object):
    def isParlindrome(self, s):
        return s == s[::-1]
    
    def dfs(self, s, soln):
        if len(s) == 0:
            self.solns.append(soln)
        for i in range(1, len(s) + 1):
            if self.isParlindrome(s[:i]):
                self.dfs(s[i:], soln + [s[:i]])

    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        if s is None:
            return []
        self.solns = []
        self.dfs(s, [])
        return self.solns

a = Solution()
print(a.partition("aab"))
