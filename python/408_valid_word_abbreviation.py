"""
Given a non-empty string s and an abbreviation abbr, return whether the string
matches with the given abbreviation.

A string such as "word" contains only the following valid abbreviations:

["word", "1ord", "w1rd", "wo1d", "wor1", "2rd", "w2d", "wo2", "1o1d", "1or1",
"w1r1", "1o2", "2r1", "3d", "w3", "4"] 

Notice that only the above abbreviations are valid abbreviations of the string
"word". Any other string is not a valid abbreviation of "word".

Note:
    Assume s contains only lowercase letters and abbr contains only lowercase
    letters and digits.

Example 1:
    Given s = "internationalization", abbr = "i12iz4n":

    Return true.

Example 2:
    Given s = "apple", abbr = "a2e":

    Return false.
"""
class Solution(object):
    def validWordAbbreviation(self, word, abbr):
        """
        :type word: str
        :type abbr: str
        :rtype: bool
        """
        nums = set([str(i) for i in range(10)])
        digits = []
        loc = -1
        for c in abbr:
            if c in nums:
                if c == '0' and digits == []:
                    return False
                digits.append(c)
            else:
                if digits:
                    loc += int("".join(digits))
                    digits = []
                loc += 1
                if loc >= len(word):
                    return False
                if c != word[loc]:
                    return False
        if digits:
            loc += int("".join(digits))
        return loc == len(word) - 1

assert Solution().validWordAbbreviation("a", "2") == False
assert Solution().validWordAbbreviation("word", "w2d") == True
assert Solution().validWordAbbreviation("internationalization", "i12iz4n") == True
assert Solution().validWordAbbreviation("apple", "a3e") == True
assert Solution().validWordAbbreviation("apple", "a2e") == False
print("408 all test cases passed")
