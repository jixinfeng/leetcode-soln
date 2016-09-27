"""
Given n non-negative integers representing an elevation map where the width of
each bar is 1, compute how much water it is able to trap after raining.

For example, 
    Given [0,1,0,2,1,0,1,3,2,1,2,1], return 6.

    ![Sample Image](http://www.leetcode.com/wp-content/uploads/2012/08/rainwatertrap.png)

"""
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if height is None or height == []:
            return 0
        vol = 0
        left, right = 0, len(height) - 1
        leftMax, rightMax = 0, len(height) - 1
        while left < right:
            if height[left] <= height[right]:
                vol += max(0, height[leftMax] - height[left])
                if height[left] > height[leftMax]:
                    leftMax = left
                left += 1
            else:
                vol += max(0, height[rightMax] - height[right])
                if height[right] > height[rightMax]:
                    rightMax = right
                right -= 1
        return vol

a = Solution()
height = [0,1,0,2,1,0,1,3,2,1,2,1]
print(a.trap(height))
