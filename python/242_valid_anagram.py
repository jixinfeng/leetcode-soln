"""
Given two strings s and t, write a function to determine if t is an anagram of s.

For example,
s = "anagram", t = "nagaram", return true.
s = "rat", t = "car", return false.

Note:
    You may assume the string contains only lowercase alphabets.

Follow up:
    What if the inputs contain unicode characters? How would you adapt your solution to such case?
"""


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if s == t:
            return True
        if len(s) != len(t):
            return False

        char_count = {}
        for c in s:
            char_count[c] = char_count.get(c, 0) + 1

        for c in t:
            char_count[c] = char_count.get(c, 0) - 1

        return not any(char_count.values())
