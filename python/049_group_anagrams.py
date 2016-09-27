"""
Given an array of strings, group anagrams together.

For example, given: ["eat", "tea", "tan", "ate", "nat", "bat"], 
Return:

[
  ["ate", "eat","tea"],
  ["nat","tan"],
  ["bat"]
]

Note: All inputs will be in lower-case.
"""
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        if strs is None or strs == []:
            return []
        soln = {}
        for s in strs:
            key = ''.join(sorted(list(s)))
            if key in soln:
                soln[key].append(s)
            else:
                soln[key] = [s]
        return list(soln.values())

a = Solution()
print(a.groupAnagrams(["", ""]))
print(a.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
print(a.groupAnagrams(["tea","","eat","","tea",""]))
