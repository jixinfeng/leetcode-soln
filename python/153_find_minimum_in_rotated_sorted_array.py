"""
Suppose a sorted array is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Find the minimum element.

You may assume no duplicate exists in the array.
"""
class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums is None or nums == []:
            return None
        left, right = 0, len(nums) - 1
        minElement = nums[-1]
        while left < right - 1:
            middle = left + (right - left) // 2
            if nums[middle] > minElement:
                left = middle
            else:
                right = middle
                minElement = nums[middle]
        if nums[left] < minElement:
            return nums[left]
        else:
            return nums[right]

a = Solution()
print(a.findMin([4,5,6,7,0,1,2]))
