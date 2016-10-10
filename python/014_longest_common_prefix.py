"""
Write a function to find the longest common prefix string amongst an array of strings.
"""
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if strs is None or strs == "":
            return ""
        lcp = list(strs[0])
        for i, string in enumerate(strs):
            if list(string[0:len(lcp)]) == lcp:
                continue
            else:
                while len(lcp) > 0 and list(string[0:len(lcp)]) != lcp:
                    lcp.pop()
                if lcp == 0:
                    return ""
        return "".join(lcp)

a = Solution()
print(a.longestCommonPrefix(["apps","apple","append"]) == "app")
