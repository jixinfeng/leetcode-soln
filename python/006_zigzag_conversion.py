"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of
rows like this: (you may want to display this pattern in a fixed font for better
legibility)

    P   A   H   N
    A P L S I I G
    Y   I   R

And then read line by line: "PAHNAPLSIIGYIR"
Write the code that will take a string and make this conversion given a number
of rows:
    string convert(string text, int nRows);
    convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".
"""
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1 or numRows > len(s):
            return s
        soln = [[] for i in range(numRows)]
        for i in range(len(s)):
            loc = i % (numRows * 2 - 2)
            if loc < numRows:
                soln[loc].append(s[i])
            else:
                soln[-(loc - numRows + 2)].append(s[i])
        return "".join(["".join(soln[i]) for i in range(numRows)])

a = Solution()
print(a.convert("ABCD", 1) == "ABCD")
print(a.convert("ABCD", 5) == "ABCD")
print(a.convert("ABCD", 3) == "ABDC")
print(a.convert("PAYPALISHIRING", 3) == "PAHNAPLSIIGYIR")
