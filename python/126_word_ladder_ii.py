"""
Given two words (beginWord and endWord), and a dictionary's word list, find all
shortest transformation sequence(s) from beginWord to endWord, such that:

Only one letter can be changed at a time Each transformed word must exist in the
word list. Note that beginWord is not a transformed word.
For example,

Given:
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot","dot","dog","lot","log","cog"]
Return:
    [
        ["hit","hot","dot","dog","cog"],
        ["hit","hot","lot","log","cog"]
    ]
Note:
    Return an empty list if there is no such transformation sequence.
    All words have the same length.
    All words contain only lowercase alphabetic characters.
    You may assume no duplicates in the word list.
    You may assume beginWord and endWord are non-empty and are not the the same.

UPDATE (2017/1/20):
The wordList parameter had been changed to a list of strings (instead of a set
of strings). Please reload the code definition to get the latest changes.
"""


# TODO: TLE, need revision
class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        if endWord not in wordList:
            return []
        minLength = len(wordList)
        paths = collections.deque([[[beginWord], 1]])
        neighbors = collections.defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                key = word[:i] + '_' + word[i + 1:]
                neighbors[key].append(word)
        while paths:
            currPath, pLength = paths.popleft()
            currWord = currPath[-1]
            visited = set(currPath)
            if currWord == endWord:
                paths.appendleft([currPath, pLength])
                minLength = min(pLength, minLength)
                break
            if self.wordDist(currWord, endWord) <= 1:
                paths.append([currPath + [endWord], pLength + 1])
                minLength = min(pLength + 1, minLength)
            else:
                for i in range(len(currWord)):
                    searchKey = currWord[:i] + '_' + currWord[i + 1:]
                    for nextWord in neighbors[searchKey]:
                        if nextWord not in visited:
                            visited.add(nextWord)
                            paths.append([currPath + [nextWord], pLength + 1])
        soln = []
        for path in paths:
            if path[0][-1] == endWord and \
               path[1] == minLength:
                soln.append(path[0])
        return soln

    def wordDist(self, w1, w2):
        return sum([w1[i] != w2[i] for i in range(len(w1))])


import collections
a = Solution()
print(a.findLadders("hit", 
                    "cog", 
                    ["hot", "dot", "dog", "lot", "log", "cog"]) == [
                        ["hit", "hot", "dot", "dog", "cog"],
                        ["hit", "hot", "lot", "log", "cog"]
                    ])
print(a.findLadders("red",
                    "tax",
                    ["ted", "tex", "red", "tax", "tad", "den", "rex", "pee"]) == [
                        ["red", "ted", "tad", "tax"],
                        ["red", "ted", "tex", "tax"],
                        ["red", "rex", "tex", "tax"]
                    ])
