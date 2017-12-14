"""
Given an array and a value, remove all instances of that value in place and
return the new length.

Do not allocate extra space for another array, you must do this in place with
constant memory.

The order of elements can be changed. It doesn't matter what you leave beyond
the new length.

Example:
    Given input array nums = [3,2,2,3], val = 3

    Your function should return length = 2, with the first two elements of nums
    being 2.

Hint:

    Try two pointers.
    Did you use the property of "the order of elements can be changed"?
    What happens when the elements to remove are rare?
"""
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if nums is None or nums == []:
            return 0
        if val not in nums:
            return len(nums)
        slow, fast = 0, 0
        for fast, fast_val in enumerate(nums):
            if fast_val == val:
                continue
            else:
                nums[slow] = nums[fast]
                slow += 1
        return slow

a = Solution()
print(a.removeElement([3], 3) == 0)
print(a.removeElement([2], 3) == 1)
print(a.removeElement([3, 2, 2, 3], 3) == 2)
print(a.removeElement([3, 3, 2, 3], 3) == 1)
print(a.removeElement([3, 2, 2, 3], 3) == 2)
print(a.removeElement([3, 3, 3, 3], 3) == 0)
