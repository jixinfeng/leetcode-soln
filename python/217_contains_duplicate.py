"""
Given an array of integers, find if the array contains any duplicates. Your
function should return true if any value appears at least twice in the array,
and it should return false if every element is distinct.
"""
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        numsset = set()
        for num in nums:
            if num in numsset:
                return True
            else:
                numsset.add(num)
        return False

"""
One-liner solutions
    def containsDuplicate(self, nums):
        return False if nums == [] else collections.Counter(nums).most_common(1)[0][1] > 1
or
    def containsDuplicate(self, nums):
        return len(nums) > len(set(nums))
"""
