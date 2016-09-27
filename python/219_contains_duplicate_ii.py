"""
Given an array of integers and an integer k, find out whether there are two
distinct indices i and j in the array such that nums[i] = nums[j] and the
difference between i and j is at most k.
"""
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        loc={}
        for i,num in enumerate(nums):
            j=loc.get(num,-1)
            if j>=0 and i-j<=k:
                return True
            loc[num]=i
        return False
