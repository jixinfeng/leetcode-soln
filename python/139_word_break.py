"""
Given a string s and a dictionary of words dict, determine if s can be segmented
into a space-separated sequence of one or more dictionary words.

For example, given
s = "leetcode",
dict = ["leet", "code"].

Return true because "leetcode" can be segmented as "leet code".
"""
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: bool
        """
        if s is None or s == "":
            return True
        if wordDict is None or wordDict == []:
            return False
        dp = [False for i in range(len(s) + 1)]
        dp[0] = True
        for i in range(1, len(s) + 1):
            for j in range(i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    break
        return dp[-1]

a = Solution()
print(a.wordBreak("leetcode", set(["leet", "code"])))
print(a.wordBreak("leet1code", set(["leet", "code"])))
print(a.wordBreak("aaaaaaa", set(["aaaa", "aaa"])))
