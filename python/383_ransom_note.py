"""
Given an arbitrary ransom note string and another string containing letters from
all the magazines, write a function that will return true if the ransom  note
can be constructed from the magazines ; otherwise, it will return false.

Each letter in the magazine string can only be used once in your ransom note.

Note:
    You may assume that both strings contain only lowercase letters.
    
    canConstruct("a", "b") -> false
    canConstruct("aa", "ab") -> false
    canConstruct("aa", "aab") -> true
"""
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        if ransomNote is None or ransomNote == []:
            return True
        if magazine is None or magazine == []:
            return False
        magCount = collections.defaultdict(int)
        for c in magazine:
            magCount[c] += 1
        for c in ransomNote:
            if c not in magCount:
                return False
            elif magCount[c] <= 0:
                return False
            magCount[c] -= 1
        return True

import collections
a = Solution()
print(a.canConstruct('a','b'))
print(a.canConstruct('aa','ab'))
print(a.canConstruct('aa','aab'))
