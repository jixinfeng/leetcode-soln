"""
Write a function to generate the generalized abbreviations of a word.

Example:
    Given word = "word", return the following list (order does not matter):
        ["word", "1ord", "w1rd", "wo1d", "wor1", "2rd", "w2d", "wo2", "1o1d",
        "1or1", "w1r1", "1o2", "2r1", "3d", "w3", "4"]
"""
class Solution(object):
    def generateAbbreviations(self, word):
        """
        :type word: str
        :rtype: List[str]
        """
        if word is None or word == "":
            return [""]
        abbrevs = []
        for i in range(2 ** len(word)):
            binary = bin(i)[2:].zfill(len(word))
            abbrev = []
            countZeros = 0
            for j in range(len(word)):
                if binary[j] == '0':
                    if countZeros > 0:
                        abbrev.append(str(countZeros))
                        countZeros = 0
                    abbrev.append(word[j])
                else:
                    countZeros += 1
            if countZeros > 0:
                abbrev.append(str(countZeros))
                countZeros = 0
            abbrevs.append(''.join(abbrev))
        return abbrevs

a = Solution()
print(a.generateAbbreviations('python'))
print(a.generateAbbreviations('hello'))
print(a.generateAbbreviations('word'))
