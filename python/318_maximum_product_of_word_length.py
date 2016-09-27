"""
Given a string array words, find the maximum value of length(word[i]) *
length(word[j]) where the two words do not share common letters. You may assume
that each word will contain only lower case letters. If no such two words exist,
return 0.

Example 1:
    Given ["abcw", "baz", "foo", "bar", "xtfn", "abcdef"]
    Return 16
    The two words can be "abcw", "xtfn".

Example 2:
    Given ["a", "ab", "abc", "d", "cd", "bcd", "abcd"]
    Return 4
    The two words can be "ab", "cd".

Example 3:
    Given ["a", "aa", "aaa", "aaaa"]
    Return 0
    No such pair of words.

Credits:
    Special thanks to @dietpepsi for adding this problem and creating all test cases.
"""
class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        if words is None or words == []:
            return 0
        length = len(words)
        wLengths = [len(word) for word in words]
        wInts = []
        for word in words:
            wInt = 0
            for c in word:
                wInt |= 1 << ord(c) - ord('a')
            wInts.append(wInt)
        return max([wLengths[i] * wLengths[j] 
                    for i in range(length)
                    for j in range(i + 1, length)
                    if not wInts[i] & wInts[j]]
                   or [0])

a = Solution()
print(a.maxProduct(["abcw", "baz", "foo", "bar", "xtfn", "abcdef"]) == 16)
print(a.maxProduct(["a", "ab", "abc", "d", "cd", "bcd", "abcd"]) == 4)
print(a.maxProduct(["a", "aa", "aaa", "aaaa"]) == 0)
