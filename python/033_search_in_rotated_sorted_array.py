"""
Suppose a sorted array is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

You are given a target value to search. If found in the array return its index,
otherwise return -1.

You may assume no duplicate exists in the array.
"""
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if nums is None or nums == []:
            return -1
        left, right = 0, len(nums) - 1
        while left < right - 1:
            middle = left + (right - left) // 2
            if nums[middle] == target:
                return middle
            elif nums[middle] > nums[left]:
                if nums[middle] > target and target >= nums[left]:
                    right = middle
                else:
                    left = middle
            else:
                if nums[middle] < target and target <= nums[right]:
                    left = middle
                else:
                    right = middle
        if nums[left] == target:
            return left
        elif nums[right] == target:
            return right
        else:
            return -1

a = Solution()
print("0, 3, 4, 6?")
print(a.search([4,5,6,7,0,1,2],4))
print(a.search([4,5,6,7,0,1,2],7))
print(a.search([4,5,6,7,0,1,2],0))
print(a.search([4,5,6,7,0,1,2],2))
