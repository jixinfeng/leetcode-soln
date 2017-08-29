"""
Implement wildcard pattern matching with support for '?' and '*'.

'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).

The matching should cover the entire input string (not partial).

The function prototype should be:
bool isMatch(const char *s, const char *p)

Some examples:
isMatch("aa","a") → false
isMatch("aa","aa") → true
isMatch("aaa","aa") → false
isMatch("aa", "*") → true
isMatch("aa", "a*") → true
isMatch("ab", "?*") → true
isMatch("aab", "c*a*b") → false
"""
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if len(p) > 1:
            plist = [p[0]]
            for c in p[1:]:
                if c == "*" and plist[-1] == "*":
                    continue
                else:
                    plist.append(c)
            p = "".join(plist)
        return self.dfs(s, p)

    def dfs(self, s, p):
        if s == "" and p == "":
            return True
        elif p == "":
            return False
        elif s == "":
            if p == "*":
                return True
            else:
                return False
        else:
            if s[0] == p[0] or p[0] == "?":
                return self.dfs(s[1:], p[1:])
            elif p[0] == "*":
                for i in range(0, len(s) - len("".join(p.split("*"))) + 1):
                    if self.dfs(s[i:], p[1:]):
                        return True
                return False
            else:
                return False

a = Solution()
assert a.isMatch("aa", "a") == False
assert a.isMatch("aa", "aa") == True
assert a.isMatch("aaa", "aa") == False
assert a.isMatch("aa", "*") == True
assert a.isMatch("aa", "a*") == True
assert a.isMatch("ab", "?*") == True
assert a.isMatch("aab", "c*a*b") == False
assert a.isMatch("c", "*?*") == True
assert a.isMatch("ho", "ho**") == True
assert a.isMatch("babaaababaabababbbbbbaabaabbabababbaababbaaabbbaaab",
                 "***bba**a*bbba**aab**b") == False
assert a.isMatch("babbbbaabababaabbababaababaabbaabababbaaababbababaaaaaabbabaaaabababbabbababbbaaaababbbabbbbbbbbbbaabbb",
                 "b**bb**a**bba*b**a*bbb**aba***babbb*aa****aabb*bbb***a") == False

