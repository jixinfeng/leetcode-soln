"""
Given a string, find the first non-repeating character in it and return it's
index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
Note: You may assume the string contain only lowercase letters.
"""
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s is None or s == '':
            return -1
        if len(s) == 1:
            return 0
        count = collections.defaultdict(int)
        unique = 0
        for i, c in enumerate(s):
            count[c] += 1
            if count[s[unique]] > 1:
                while unique < i and count[s[unique]] > 1:
                    unique += 1
        if count[s[unique]] > 1:
            return -1
        return unique

import collections
a = Solution()

print(a.firstUniqChar('cc'))
print(a.firstUniqChar('leetcode'))
print(a.firstUniqChar('loveleetcode'))
