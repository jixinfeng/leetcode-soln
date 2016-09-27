"""
Find the total area covered by two rectilinear rectangles in a 2D plane.

Each rectangle is defined by its bottom left corner and top right corner as
shown in the figure.

![Example layout]
(https://leetcode.com/static/images/problemset/rectangle_area.png)

Assume that the total area is never beyond the maximum possible value of int.

Credits:
    Special thanks to @mithmatt for adding this problem, creating the above
    image and all test cases.
"""
class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        areaA=(C-A)*(D-B)
        areaB=(G-E)*(H-F)
        if (G-A)*(E-C)>=0 or (H-B)*(F-D)>=0:
            areaO=0
        else:
            overlapX=min(abs(G-A),abs(C-E),abs(C-A),abs(G-E))
            overlapY=min(abs(H-B),abs(D-F),abs(D-B),abs(H-F))
            areaO=overlapX*overlapY
        return areaA+areaB-areaO
