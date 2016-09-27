"""
Given a digit string, return all possible letter combinations that the number
could represent.

A mapping of digit to letters (just like on the telephone buttons) is given
below.

Input:Digit string "23"
    Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

Note:
    Although the above answer is in lexicographical order, your answer could be
    in any order you want.
"""
class Solution(object):
    letters = {'2' : ['a', 'b', 'c'],
               '3' : ['d', 'e', 'f'],
               '4' : ['g', 'h', 'i'],
               '5' : ['j', 'k', 'l'],
               '6' : ['m', 'n', 'o'],
               '7' : ['p', 'q', 'r', 's'],
               '8' : ['t', 'u', 'v'],
               '9' : ['w', 'x', 'y', 'z']}

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if digits is None or digits == '':
            return []
        if len(digits) == 1:
            return self.letters.get(digits[0], [])
        solns = []
        if digits[0] in self.letters:
            for soln in self.letterCombinations(digits[1:]):
                for ch in self.letters[digits[0]]:
                    solns.append(ch + soln)
        else:
            for soln in self.letterCombinations(digits[1:]):
                solns.append(soln)
        return solns

a = Solution()
print(a.letterCombinations('123'))
