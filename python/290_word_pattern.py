"""
Given a pattern and a string s, find if s follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.

Example 1:

Input: pattern = "abba", s = "dog cat cat dog"
Output: true
Example 2:

Input: pattern = "abba", s = "dog cat cat fish"
Output: false
Example 3:

Input: pattern = "aaaa", s = "dog cat cat dog"
Output: false


Constraints:

1 <= pattern.length <= 300
pattern contains only lower-case English letters.
1 <= s.length <= 3000
s contains only lowercase English letters and spaces ' '.
s does not contain any leading or trailing spaces.
All the words in s are separated by a single space.
"""


class Solution(object):
    def wordPattern(self, pattern: str, s: str) -> bool:
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        words = s.split(' ')
        if len(pattern) != len(words):
            return False
        charMap = {}
        wordMap = {}
        for c, w in zip(pattern, words):
            if c not in charMap.keys():
                charMap[c] = w
            else:
                if charMap[c] != w:
                    return False
            if w not in wordMap.keys():
                wordMap[w] = c
            else:
                if wordMap[w] != c:
                    return False
        return True


a = Solution()
print(a.wordPattern('abba', "dog cat cat dog"))
print(a.wordPattern('abba', "dog cat cat fish"))
print(a.wordPattern('aaaa', "dog cat cat dog"))
print(a.wordPattern('abba', "dog dog dog dog"))
