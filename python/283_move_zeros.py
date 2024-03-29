"""
Given an array nums, write a function to move all 0's to the end of it while
maintaining the relative order of the non-zero elements.

For example, given nums = [0, 1, 0, 3, 12], after calling your function, nums
should be [1, 3, 12, 0, 0].

Note:
    You must do this in-place without making a copy of the array.
    Minimize the total number of operations.

Credits:
    Special thanks to @jianchao.li.fighter for adding this problem and
    creating all test cases.
"""


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        reader_index, writer_index = 0, 0
        while reader_index < len(nums):
            if nums[reader_index] == 0:
                reader_index += 1
            else:
                nums[writer_index] = nums[reader_index]
                reader_index += 1
                writer_index += 1

        while writer_index < len(nums):
            nums[writer_index] = 0
            writer_index += 1
