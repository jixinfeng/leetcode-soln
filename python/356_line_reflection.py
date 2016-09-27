"""
Given n points on a 2D plane, find if there is such a line parallel to y-axis
that reflect the given points.

Example 1:
    Given points = [[1,1],[-1,1]], return true.

Example 2:
    Given points = [[1,1],[-1,-1]], return false.

Follow up:
    Could you do better than O(n2)?

Hint:

    Find the smallest and largest x-value for all points.

    If there is a line then it should be at y = (minX + maxX) / 2.

    For each point, make sure that it has a reflected point in the opposite
    side.

Credits:
    Special thanks to @memoryless for adding this problem and creating all test
    cases.
"""
class Solution(object):
    def isReflected(self, points):
        """
        :type points: List[List[int]]
        :rtype: bool
        """
        if points is None:
            return False
        if not points:
            return True
        X = min(points)[0] + max(points)[0]
        return {(x, y) for x, y in points} == {(X - x, y) for x, y in points}

a = Solution()
print(a.isReflected([[1, 1], [-1, 1]]) == True)
print(a.isReflected([[1, 1], [-1, -1]]) == False)
print(a.isReflected([[0,0],[1,0],[3,0]]) == False)
print(a.isReflected([[-16,1],[16,1],[16,1]]) == True)

"""
Note:
    https://discuss.leetcode.com/topic/47843/1-line-ruby-2-lines-python/2
"""
