"""
Related to question Excel Sheet Column Title

Given a column title as appear in an Excel sheet, return its corresponding
column number.

For example:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28 

Credits:
    Special thanks to @ts for adding this problem and creating all test cases.
"""
class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        column = 0
        for i, char in enumerate(s[::-1]):
            column += (ord(char) - 64) * pow(26, i)
        return column
