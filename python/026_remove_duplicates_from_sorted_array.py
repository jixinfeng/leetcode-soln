"""
Given a sorted array, remove the duplicates in place such that each element
appear only once and return the new length.

Do not allocate extra space for another array, you must do this in place with
constant memory.

For example,
Given input array nums = [1,1,2],

Your function should return length = 2, with the first two elements of nums
being 1 and 2 respectively. It doesn't matter what you leave beyond the new
length.
"""
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 1:
            return len(nums)
        l = len(nums)
        slow = 0
        for fast in range(l):
            if nums[fast] != nums[slow]:
                slow += 1
            nums[slow] = nums[fast]
        return slow + 1

a = Solution()
print(a.removeDuplicates([1, 1]) == 1)
print(a.removeDuplicates([1, 1, 2]) == 2)
print(a.removeDuplicates([1, 1, 2, 2, 3, 3, 3, 4]) == 4)
