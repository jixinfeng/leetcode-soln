"""
Given two strings S and T, determine if they are both one edit distance apart.
"""
class Solution(object):
    def isOneEditDistance(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        m = len(s)
        n = len(t)
        if m > n + 1 or n > m + 1:
            return False
        elif m == n:
            diff = 0
            for i in range(m):
                if s[i] != t[i]:
                    diff += 1
            return diff == 1
        else:
            loc = -1
            for i in range(min(m, n)):
                if s[i] != t[i]:
                    loc = i
                    break
            if loc == -1:
                return True
            else:
                if m > n:
                    return "".join([s[i] for i in range(m) if i != loc]) == t
                else:
                    return "".join([t[i] for i in range(n) if i != loc]) == s

a = Solution()
print(a.isOneEditDistance("ac", "a"))
