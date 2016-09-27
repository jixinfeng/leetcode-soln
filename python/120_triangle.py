"""
Given a triangle, find the minimum path sum from top to bottom. Each step you
may move to adjacent numbers on the row below.

For example, given the following triangle

    [
         [2],
        [3,4],
       [6,5,7],
      [4,1,8,3]
    ]

The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).

Note:
Bonus point if you are able to do this using only O(n) extra space, where n is
the total number of rows in the triangle.

In oldMinSum=newMinSum[:] the [:] can not be omitted.
"""
class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        if triangle is None or triangle == []:
            return 0
        height = len(triangle)
        newMinSum = [0] * height
        for row in triangle:
            oldMinSum = newMinSum[:]    #deep copy
            for i in range(len(row)):
                if i == 0:
                    newMinSum[i] = oldMinSum[i] + row[i]
                elif i == len(row) - 1:
                    newMinSum[i] = oldMinSum[i - 1] + row[i]
                else:
                    newMinSum[i] = min(oldMinSum[i], oldMinSum[i - 1]) + row[i]
        return min(newMinSum)

a = Solution()
print(a.minimumTotal([[-1],[2,3],[1,-1,-3]]))
