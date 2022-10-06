"""
This is a follow up of Shortest Word Distance. The only difference is now you
are given the list of words and your method will be called repeatedly many times
with different parameters. How would you optimize it?

Design a class which receives a list of words in the constructor, and implements
a method that takes two words word1 and word2 and return the shortest distance
between these two words in the list.

For example,

    Assume that words = ["practice", "makes", "perfect", "coding", "makes"].

    Given word1 = “coding”, word2 = “practice”, return 3.
    Given word1 = "makes", word2 = "coding", return 1.

Note:
    You may assume that word1 does not equal to word2, and word1 and word2 are
    both in the list.
"""


class WordDistance:

    def __init__(self, wordsDict: List[str]):
        self.locations = {}
        for i, word in enumerate(wordsDict):
            self.locations[word] = self.locations.get(word, []) + [i]

    def shortest(self, word1: str, word2: str) -> int:
        word_1_locs = self.locations[word1]
        word_2_locs = self.locations[word2]

        return min([abs(l1 - l2) for l1 in word_1_locs for l2 in word_2_locs])


a = WordDistance(["practice", "makes", "perfect", "coding", "makes"])
print(a.shortest("coding", "practice"))
print(a.shortest("makes", "coding"))

b = WordDistance(["a", "a", "b", "b"])
print(b.shortest("a", "b"))
print(b.shortest("b", "a"))

# Your WordDistance object will be instantiated and called as such:
# wordDistance = WordDistance(words)
# wordDistance.shortest("word1", "word2")
# wordDistance.shortest("anotherWord1", "anotherWord2")
