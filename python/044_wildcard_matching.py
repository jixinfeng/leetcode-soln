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
import unittest


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


class TestSolution(unittest.TestCase):
    def test_char_only_neq(self):
        self.assertFalse(Solution().isMatch("aa", "a"))

    def test_char_only_eq(self):
        self.assertTrue(Solution().isMatch("aa", "aa"))

    def test_q_mark_eq(self):
        self.assertTrue(Solution().isMatch("ab", "a?"))

    def test_q_mark_neq(self):
        self.assertFalse(Solution().isMatch("abc", "a?"))

    def test_star_eq(self):
        self.assertTrue(Solution().isMatch("c", "*?*"))

    def test_star_neq(self):
        self.assertFalse(Solution().isMatch("aab", "c*a*b"))

    def test_long_case(self):
        self.assertFalse(Solution().isMatch("babaaababaabababbbbbbaabaabbabababbaababbaaabbbaaab",
                                            "***bba**a*bbba**aab**b"))

    def test_long_case(self):
        self.assertFalse(Solution().isMatch("babbbbaabababaabbababaababaabbaabababbaaababbababaaaaaabbabaaaabababbabbababbbaaaababbbabbbbbbbbbbaabbb",
                                            "b**bb**a**bba*b**a*bbb**aba***babbb*aa****aabb*bbb***a"))

unittest.main()

