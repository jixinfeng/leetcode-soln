"""
An abbreviation of a word follows the form <first letter><number><last letter>.
Below are some examples of word abbreviations:

    a) it                      --> it    (no abbreviation)
    
         1
    b) d|o|g                   --> d1g
    
                  1    1  1
         1---5----0----5--8
    c) i|nternationalizatio|n  --> i18n
    
                  1
         1---5----0
    d) l|ocalizatio|n          --> l10n

Assume you have a dictionary and given a word, find whether its abbreviation is
unique in the dictionary. A word's abbreviation is unique if no other word from
the dictionary has the same abbreviation.

Example: 
    Given dictionary = [ "deer", "door", "cake", "card" ]

    isUnique("dear") -> false
    isUnique("cart") -> true
    isUnique("cane") -> false
    isUnique("make") -> true
"""


class ValidWordAbbr(object):
    def __init__(self, dictionary: List[str]):
        """
        initialize your data structure here.
        :type dictionary: List[str]
        """
        self.abbrevs = collections.defaultdict(list)
        for word in set(dictionary):
            abbr = self.getAbbr(word)
            self.abbrevs[abbr].append(word)

    def getAbbr(self, word):
        if len(word) <= 2:
            return word
        else:
            return "".join([word[0], str(len(word) - 2), word[-1]])

    def isUnique(self, word: str) -> bool:
        """
        check if a word is unique.
        :type word: str
        :rtype: bool
        """
        abbr = self.getAbbr(word)
        value = self.abbrevs.get(abbr, None)
        return value is None or value == [word]


import collections

a = ValidWordAbbr(["deer", "door", "cake", "card"])
print(a.isUnique("dear"))
print(a.isUnique("cart"))
print(a.isUnique("cane"))
print(a.isUnique("make"))

a = ValidWordAbbr(["hello"])
print(a.isUnique("hello"))

a = ValidWordAbbr(["deer", "door", "cake", "card"])
print(a.isUnique("deer"))
print(a.isUnique("door"))
print(a.isUnique("card"))
print(a.isUnique("cake"))

a = ValidWordAbbr(["a", "a"])
print(a.isUnique("a"))

# Your ValidWordAbbr object will be instantiated and called as such:
# vwa = ValidWordAbbr(dictionary)
# vwa.isUnique("word")
# vwa.isUnique("anotherWord")
