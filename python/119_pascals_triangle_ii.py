"""
Given an index k, return the kth row of the Pascal's triangle.

For example, given k = 3,
Return [1,3,3,1].

Note:
    Could you optimize your algorithm to use only O(k) extra space?
"""
class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        rowIndex+=1
        if rowIndex==0:
            return []
        if rowIndex==1:
            return [1]
        oldRow=[]
        for row in range(1,rowIndex+1):
            newRow=[]
            for entry in range(1,row+1):
                if entry==1 or entry==row:
                    newRow.append(1)
                else:
                    newRow.append(oldRow[entry-2]+oldRow[entry-1])
            oldRow=newRow
        return newRow
