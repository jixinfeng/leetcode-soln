"""
A peak element is an element that is greater than its neighbors.

Given an input array where num[i] ≠ num[i+1], find a peak element and return its
index.

The array may contain multiple peaks, in that case return the index to any one
of the peaks is fine.

You may imagine that num[-1] = num[n] = -∞.

For example, in array [1, 2, 3, 1], 3 is a peak element and your function should
return the index number 2.

Note:
    Your solution should be in logarithmic complexity.

Credits:
    Special thanks to @ts for adding this problem and creating all test cases.
"""
class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums is None or nums == []:
            return -1
        if len(nums) == 1:
            return 0
        if len(nums) == 2:
            return [0, 1][nums[0] < nums[1]]
        if nums[0] > nums[1]:
            return 0
        if nums[-1] > nums[-2]:
            return len(nums) - 1
        left, right = 0, len(nums) - 1
        while left < right - 1:
            middle = left + (right - left) // 2
            #print(left, middle, right)
            if nums[middle] > nums[middle - 1] and \
               nums[middle] > nums[middle + 1]:
                return middle
            elif nums[middle] > nums[middle - 1]:
                left = middle
            elif nums[middle] > nums[middle + 1]:
                right = middle
            elif nums[middle] < nums[middle - 1]:
                right = middle
            elif nums[middle] < nums[middle + 1]:
                left = middle

        if nums[left] > nums[left - 1] and \
           nums[left] > nums[left + 1]:
            return left
        if nums[right] > nums[right - 1] and \
           nums[right] > nums[right + 1]:
            return right

a=Solution()
print(a.findPeakElement([1,2]))
print(a.findPeakElement([3,2,1]))
print(a.findPeakElement([1,2,3]))
print(a.findPeakElement([1,2,3,1]))
print(a.findPeakElement([1,2,5,4,3,2,1]))
print(a.findPeakElement([1,2,1,2,1]))
