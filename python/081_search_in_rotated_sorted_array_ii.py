"""
Follow up for "Search in Rotated Sorted Array":
What if duplicates are allowed?

Would this affect the run-time complexity? How and why?

Write a function to determine if a given target is in the array.
"""
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        if nums is None or nums == []:
            return False
        l = len(nums)
        left, right = 0, l - 1
        while left < right and nums[left] == nums[right]:
            right -= 1
        if nums[left] == target or nums[right] == target:
            return True
        while left + 1 < right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return True
            elif nums[mid] >= nums[left]:
                if nums[mid] > target and target >= nums[left]:
                    right = mid
                else:
                    left = mid
            else:
                if nums[mid] < target and target <= nums[right]:
                    left = mid
                else:
                    right = mid
        if nums[left] == target or nums[right] == target:
            return True
        else:
            return False

a = Solution()
print(a.search([3,4,4,4,5,6,7,1,1,1,2,3,3,3,3], 7))
print(a.search([2,2,2,0,0,1], 0))
