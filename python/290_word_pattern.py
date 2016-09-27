"""
Given a pattern and a string str, find if str follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter
in pattern and a non-empty word in str.

Examples:
    pattern = "abba", str = "dog cat cat dog" should return true.
    pattern = "abba", str = "dog cat cat fish" should return false.
    pattern = "aaaa", str = "dog cat cat dog" should return false.
    pattern = "abba", str = "dog dog dog dog" should return false.

Notes:
    You may assume pattern contains only lowercase letters, and str contains
    lowercase letters separated by a single space.

Credits:
    Special thanks to @minglotus6 for adding this problem and creating all test
    cases.
"""
class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        words=str.split(' ')
        if len(pattern)!=len(words):
            return False
        charMap={}
        wordMap={}
        for c,w in zip(pattern,words):
            if c not in charMap.keys():
                charMap[c]=w
            else:
                if charMap[c]!=w:
                    return False
            if w not in wordMap.keys():
                wordMap[w]=c
            else:
                if wordMap[w]!=c:
                    return False
        return True

a=Solution()
print(a.wordPattern('abba',"dog cat cat dog"))
print(a.wordPattern('abba',"dog cat cat fish"))
print(a.wordPattern('aaaa',"dog cat cat dog"))
print(a.wordPattern('abba',"dog dog dog dog"))

"""
two shorter solutions:

def wordPattern(self, pattern, str):
    s = pattern
    t = str.split()
    return map(s.find, s) == map(t.index, t)

def wordPattern(self, pattern, str):
    s = pattern
    t = str.split()
    return len(set(zip(s, t))) == len(set(s)) == len(set(t)) and len(s)==len(t)
"""
