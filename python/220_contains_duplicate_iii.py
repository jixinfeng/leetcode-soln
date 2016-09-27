"""
Given an array of integers, find out whether there are two distinct indices i
and j in the array such that the difference between nums[i] and nums[j] is at
most t and the difference between i and j is at most k.
"""
class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        if nums is None or nums == []:
            return False
        if k < 1 or t < 0:
            return False
        buckets = collections.defaultdict(int)
        length = len(nums)
        width = t + 1
        for i in range(length):
            key = nums[i] // width
            if key in buckets:
                return True
            if key - 1 in buckets and abs(nums[i] - buckets[key - 1]) < width:
                return True
            if key + 1 in buckets and abs(nums[i] - buckets[key + 1]) < width:
                return True
            buckets[key] = nums[i]
            if i >= k:
                del buckets[nums[i - k] // width]
        return False

import collections
a = Solution()
print(a.containsNearbyAlmostDuplicate([-1, -1], 1, 0))
print(a.containsNearbyAlmostDuplicate([1, 3, 1], 1, 1))
print(a.containsNearbyAlmostDuplicate([10, 20, 30, 25, 50], 2, 6))

"""
Note:
The idea is like the bucket sort algorithm. Suppose we have consecutive buckets
covering the range of nums with each bucket a width of (t+1). If there are two
item with difference <= t, one of the two will happen:

    (1) the two in the same bucket
    (2) the two in neighbor buckets

https://discuss.leetcode.com/topic/27608/java-python-one-pass-solution-o-n-time-o-n-space-using-buckets
"""
