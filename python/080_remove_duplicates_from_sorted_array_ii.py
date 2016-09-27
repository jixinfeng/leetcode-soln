"""
Follow up for "Remove Duplicates":
What if duplicates are allowed at most twice?

For example,
Given sorted array nums = [1,1,1,2,2,3],

Your function should return length = 5, with the first five elements of nums
being 1, 1, 2, 2 and 3. It doesn't matter what you leave beyond the new length.
"""
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums is None:
            return 0
        l = len(nums)
        if l <= 2:
            return l
        tail = 1
        dup = 1
        for i in range(1, l):
            if nums[i] == nums[i - 1]:
                dup += 1
            else:
                dup = 1
            if dup <= 2:
                nums[tail] = nums[i]
                tail += 1
        while len(nums) > tail:
            nums.pop()
        return len(nums)

a = Solution()
print(a.removeDuplicates([1,1,1,2,2,2,3,3,3]))
