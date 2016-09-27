"""
Given numRows, generate the first numRows of Pascal's triangle.

For example, given numRows = 5,
Return
    [
         [1],
        [1,1],
       [1,2,1],
      [1,3,3,1],
     [1,4,6,4,1]
    ]
"""
class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows==0:
            return []
        if numRows==1:
            return [[1]]
        pt=[]
        for level in range(1,numRows+1):
            row=[]
            for entry in range(1,level+1):
                if entry==1 or entry==level:
                    row.append(1)
                else:
                    row.append(pt[level-2][entry-2]+pt[level-2][entry-1])
            pt.append(row)
        return pt
