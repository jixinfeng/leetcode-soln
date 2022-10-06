"""
Given a pattern and a string s, return true if s matches the pattern.

A string s matches a pattern if there is some bijective mapping of single characters to strings such that if each character in pattern is replaced by the string it maps to, then the resulting string is s. A bijective mapping means that no two characters map to the same string, and no character maps to two different strings.



Example 1:

Input: pattern = "abab", s = "redblueredblue"
Output: true
Explanation: One possible mapping is as follows:
'a' -> "red"
'b' -> "blue"
Example 2:

Input: pattern = "aaaa", s = "asdasdasdasd"
Output: true
Explanation: One possible mapping is as follows:
'a' -> "asd"
Example 3:

Input: pattern = "aabb", s = "xyzabcxzyabc"
Output: false


Constraints:

1 <= pattern.length, s.length <= 20
pattern and s consist of only lowercase English letters.
"""


class Solution:
    def wordPatternMatch(self, pattern: str, s: str) -> bool:
        return self._wordPatternMatch(pattern, s, {}, {})

    def _wordPatternMatch(self, pattern: str, s: str, ptw: Dict, wtp: Dict) -> bool:
        if not pattern and not s:
            return True
        if not pattern or not s:
            return False

        curr_pattern = pattern[0]
        for i in range(1, len(s) + 1):
            curr_word = s[:i]
            if curr_pattern in ptw and ptw[curr_pattern] != curr_word \
                    or curr_word in wtp and wtp[curr_word] != curr_pattern:
                continue

            elif ptw.get(curr_pattern, "") == curr_word \
                    and wtp.get(curr_word, "") == curr_pattern:
                if self._wordPatternMatch(pattern[1:], s[i:], ptw, wtp):
                    return True
                else:
                    continue

            else:
                next_ptw = {**ptw, **{curr_pattern: curr_word}}
                next_wtp = {**wtp, **{curr_word: curr_pattern}}
                if self._wordPatternMatch(pattern[1:], s[i:], next_ptw, next_wtp):
                    return True

                else:
                    continue

        return False
