"""
You are given a string, s, and a list of words, words, that are all of the same
length. Find all starting indices of substring(s) in s that is a concatenation
of each word in words exactly once and without any intervening characters.

For example, given:
    s: "barfoothefoobarman"
    words: ["foo", "bar"]

You should return the indices: [0,9].
(order does not matter).
"""
class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if s == "" or words == []:
            return []
        wordLen = len(words[0])
        wordNum = len(words)
        wordSet = set(words)
        wordDict = {}
        sLen = len(s)
        for word in words:
            wordDict[word] = wordDict.get(word, 0) + 1 
        soln = []
        for start in range(wordLen):
            left = start
            currStart = start
            seenDict = {}
            seenCount = 0
            while currStart < sLen - wordLen + 1:
                currWord = s[currStart:currStart + wordLen]
                currStart += wordLen
                if currWord in wordSet:
                    seenDict[currWord] = seenDict.get(currWord, 0) + 1
                    if seenDict[currWord] <= wordDict[currWord]:
                        seenCount += 1
                    else:
                        while seenDict[currWord] > wordDict[currWord]:
                            removeWord = s[left:left + wordLen]
                            left += wordLen
                            seenDict[removeWord] -= 1
                            if seenDict[removeWord] < wordDict[removeWord]:
                                seenCount -= 1
                    if seenCount == wordNum:
                        soln.append(left)
                        removeWord = s[left:left + wordLen]
                        seenDict[removeWord] -= 1
                        left += wordLen
                        seenCount -= 1
                else:
                    seenDict = {}
                    seenCount = 0
                    left = currStart
        return soln

a = Solution()
print(a.findSubstring("barfoothefoobarman", ["foo", "bar"]) == [0, 9])
print(a.findSubstring("wordgoodgoodgoodbestword", ["word","good","best","good"]) == [8])
