"""
Given an array of integers, every element appears twice except for one. Find
that single one.

Note:
    Your algorithm should have a linear runtime complexity. Could you implement
    it without using extra memory?
"""


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return 2 * sum(set(nums)) - sum(nums)


"""
Note:
    ^ is xor operator
    0 xor x = x
    x xor x = 0
"""
