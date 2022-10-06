"""
Given a positive integer, return its corresponding column title as appear in an Excel sheet.

For example:

    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB 

Credits:
    Special thanks to @ifanchu for adding this problem and creating all test cases.
"""


class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        weights = {i: c for i, c in enumerate(string.ascii_uppercase)}
        title = []
        while columnNumber:
            columnNumber, residue = divmod(columnNumber - 1, 26)
            title.append(weights[residue])

        return "".join(title[::-1])
