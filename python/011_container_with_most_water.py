"""
Given n non-negative integers a1, a2, ..., an, where each represents a point at
coordinate (i, ai). n vertical lines are drawn such that the two endpoints of
line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis
forms a container, such that the container contains the most water.

Note: You may not slant the container.
"""
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if height is None or height == []:
            return 0
        length = len(height)
        if length == 1:
            return 0
        maxVol = 0
        left, right = 0, length - 1
        while left < right:
            maxVol = max(maxVol, (right - left) * min(height[left], height[right]))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return maxVol

a = Solution()
print(a.maxArea([1,1]) == 1)
print(a.maxArea([1]) == 0)
print(a.maxArea([1,4,4,1]) == 4)
