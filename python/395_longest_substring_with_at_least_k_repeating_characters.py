"""
Find the length of the longest substring T of a given string (consists of
lowercase letters only) such that every character in T appears no less than k
times.

Example 1:

    Input:
        s = "aaabb", k = 3
    
    Output:
        3
    
    The longest substring is "aaa", as 'a' is repeated 3 times.

Example 2:

    Input:
        s = "ababbc", k = 2
    
    Output:
        5
    
    The longest substring is "ababb", as 'a' is repeated 2 times and 'b' is
    repeated 3 times.
"""
class Solution(object):
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        if s is None or s == '':
            return 0
        if k <= 1:
            return len(s)
        counter = collections.Counter(s)
        for c in set(s):
            if counter[c] < k:
                return max([self.longestSubstring(string, k) 
                            for string in s.split(c) 
                            if len(string) > 0] or [0])
        return len(s)

import collections
a = Solution()
print(a.longestSubstring('aaabb', 3))
print(a.longestSubstring('ababbc', 2))
print(a.longestSubstring('weitong', 2))
