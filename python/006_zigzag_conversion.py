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
        if len(s)<=1 or numRows==1:
            return s
        elif numRows==2:
            return "".join([s[i] for i in range(len(s)) if i%2==0]+[s[i] for i \
                            in range(len(s)) if i%2==1])
        lines={}
        col=0
        groupSize=numRows*2-2
        for i in range(numRows):
            lines[i]=[]
        for i,c in enumerate(s):
            if col%2==0:
                lines[i%(groupSize)].append(c)
            else:
                lines[numRows-2-(i%(2*numRows-2)-numRows)].append(c)
            if i%(groupSize)==numRows-1:
                col+=1
            elif (i+1)%(groupSize)==0:
                col+=1
        return "".join(reduce(operator.add,lines.values()))

"""
Faster and shorter solution
    def convert(self, s, numRows):
        if numRows == 1 or numRows >= len(s): 
            return s
        final = [[] for row in xrange(numRows)]
        for i in range(len(s)): 
            final[numRows -1 - abs(numRows - 1 - i % (2 * numRows - 2))].append(s[i])
        return "".join(["".join(final[i]) for i in xrange(numRows)])
"""
