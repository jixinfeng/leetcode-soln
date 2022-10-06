"""
Given a list of words and two words word1 and word2, return the shortest
distance between these two words in the list.

For example,
Assume that words = ["practice", "makes", "perfect", "coding", "makes"].

Given word1 = “coding”, word2 = “practice”, return 3.
Given word1 = "makes", word2 = "coding", return 1.

Note:
    You may assume that word1 does not equal to word2, and word1 and word2 are
    both in the list.
"""


class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        loc_1 = []
        loc_2 = []
        for i, word in enumerate(wordsDict):
            if word == word1:
                loc_1.append(i)
            if word == word2:
                loc_2.append(i)

        return min([abs(l1 - l2) for l1 in loc_1 for l2 in loc_2])
