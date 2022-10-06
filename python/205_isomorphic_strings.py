"""
Given two strings s and t, determine if they are isomorphic.

Two strings are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while
preserving the order of characters. No two characters may map to the same
character but a character may map to itself.

For example,
Given "egg", "add", return true.

Given "foo", "bar", return false.

Given "paper", "title", return true.

Note:
    You may assume both s and t have the same length.
"""


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        if not (s):
            return True

        s_to_t = {}
        t_to_s = {}

        for i, chs in enumerate(s):
            cht = t[i]
            if chs in s_to_t and s_to_t[chs] != cht:
                return False
            if cht in t_to_s and t_to_s[cht] != chs:
                return False

            if chs not in s_to_t:
                s_to_t[chs] = cht
            if cht not in t_to_s:
                t_to_s[cht] = chs

        return True
