"""
Given a string s and a list of strings dict, you need to add a closed pair of
bold tag <b> and </b> to wrap the substrings in s that exist in dict. If two
such substrings overlap, you need to wrap them together by only one pair of
closed bold tag. Also, if two substrings wrapped by bold tags are consecutive,
you need to combine them.

Example 1:
Input:
s = "abcxyz123"
dict = ["abc","123"]

Output:
"<b>abc</b>xyz<b>123</b>"

Example 2:
Input:
s = "aaabbcc"
dict = ["aaa","aab","bc"]

Output:
"<b>aaabbc</b>c"

Note:
The given dict won't contain duplicates, and its length won't exceed 100.
All the strings in input have length in range [1, 1000].
"""
class Solution(object):
    def addBoldTag(self, s, dict):
        """
        :type s: str
        :type dict: List[str]
        :rtype: str
        """
        if not s or not dict:
            return s
        bold = [False] * len(s)
        word_lengths = set(map(len, dict))
        for i in range(len(s)):
            for j in word_lengths:
                curr = s[i: min(len(s), i + j)]
                if curr in dict:
                    for k in range(len(curr)):
                        bold[i + k] = True
        soln = []
        in_tag = False
        for i, is_bold in enumerate(bold):
            if is_bold and not in_tag:
                soln.append('<b>')
                in_tag = True
            elif in_tag and not is_bold:
                soln.append('</b>')
                in_tag = False
            soln.append(s[i])
        if in_tag:
            soln.append('</b>')
        return ''.join(soln)

a = Solution()
assert a.addBoldTag("abcxyz123", ["abc","123"]) == "<b>abc</b>xyz<b>123</b>"
