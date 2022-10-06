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


class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        weights = {c: i + 1 for i, c in enumerate(string.ascii_uppercase)}
        result = 0
        for ch in columnTitle:
            result = result * 26 + weights[ch]

        return result
