"""
Given a sorted array and a target value, return the index if the target is
found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

Here are few examples.
    [1,3,5,6], 5 → 2
    [1,3,5,6], 2 → 1
    [1,3,5,6], 7 → 4
    [1,3,5,6], 0 → 0
"""
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if nums is None or nums == []:
            return 0
        elif target < nums[0]:
            return 0
        elif target > nums[-1]:
            return len(nums)
        left, right = 0, len(nums)-1
        while left < right - 1:
            middle = (left + right) // 2
            if nums[middle] == target:
                return middle
            elif nums[middle] > target:
                right = middle
            else:
                left = middle
        if nums[left] == target:
            return left
        else:
            return right

a=Solution()
print(a.searchInsert([1,3,5,6],5))
print(a.searchInsert([1,3,5,6],2))
print(a.searchInsert([1,3,5,6],7))
print(a.searchInsert([1,3,5,6],0))
