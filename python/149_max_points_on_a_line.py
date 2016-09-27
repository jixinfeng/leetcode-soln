"""
Given n points on a 2D plane, find the maximum number of points that lie on the
same straight line.
"""
# Definition for a point.
class Point(object):
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b

class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        if points is None or points == []:
            return 0
        pCount = collections.defaultdict(int)
        for p in points:
            pCount[(p.x, p.y)] += 1
        if len(pCount) == 1:
            return max(pCount.values())
        lCount = collections.defaultdict(int)
        for x1, y1 in pCount:
            coefCount = collections.defaultdict(int)
            for x2, y2 in pCount:
                if x1 == x2 and y1 == y2:
                    continue
                coefCount[self.findCoef(x1, y1, x2, y2)] += pCount[(x2, y2)]
            lCount[(x1, y1)] += max(coefCount.values()) + pCount[(x1, y1)]
        return max(lCount.values())

    def gcd(self, x, y):
        if y == 0:
            return x
        else:
            return self.gcd(y, x % y)

    def findCoef(self, x1, y1, x2, y2):
        a = y2 - y1
        b = x1 - x2
        c = x2 * y1 - x1 * y2
        d = self.gcd(self.gcd(a, b), c)
        return tuple([a / d, b / d, c / d])

import collections
points1 = [Point(0, 0), Point(1, 1), Point(2, 2), Point(1, 2), Point(1, 3)]
points2 = [Point(0, 0), Point(1, 1), Point(2, 2), Point(0, 0), Point(1, 1), Point(2, 2)]
a = Solution()
print(a.maxPoints(points1))
print(a.maxPoints(points2))
