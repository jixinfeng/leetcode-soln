"""
Given an array of integers and an integer k, find out whether there are two
distinct indices i and j in the array such that nums[i] = nums[j] and the
difference between i and j is at most k.
"""


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        locations = {}
        for i, n in enumerate(nums):
            prev_locs = locations.get(n, [])
            if prev_locs and i - max(prev_locs) <= k:
                return True
            else:
                locations[n] = prev_locs + [i]

        return False
