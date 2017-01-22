"""
Given two words (beginWord and endWord), and a dictionary's word list, find
the length of shortest transformation sequence from beginWord to endWord, such
that:

    Only one letter can be changed at a time
    Each intermediate word must exist in the word list

For example,

Given:
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot","dot","dog","lot","log","cog"]
    As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
    return its length 5.

Note:
    Return 0 if there is no such transformation sequence.
    All words have the same length.
    All words contain only lowercase alphabetic characters.
"""

class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: Set[str]
        :rtype: int
        """
        if endWord not in wordList:
            return 0
        paths = deque([[beginWord, 1]])
        visited = {beginWord}
        neighbors = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                key = word[:i] + '_' + word[i + 1:]
                neighbors[key].append(word)
        while paths:
            currWord, pLength = paths.popleft()
            if self.wordDist(currWord, endWord) <= 1:
                return pLength + 1
            else:
                for i in range(len(currWord)):
                    searchKey = currWord[:i] + '_' + currWord[i + 1:]
                    for nextWord in neighbors[searchKey]:
                        if nextWord not in visited:
                            visited.add(nextWord)
                            paths.append([nextWord, pLength + 1])
        return 0

    def wordDist(self, w1, w2):
        return sum([w1[i] != w2[i] for i in range(len(w1))])

from collections import defaultdict, deque
a = Solution()
print(a.ladderLength("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]) == 5)
print(a.ladderLength("hit", "cog", ["hot", "dot", "dog", "lot", "log"]) == 0)