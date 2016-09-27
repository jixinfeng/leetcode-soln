"""
Given a sorted array of integers, find the starting and ending position of a
given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

For example,
    Given [5, 7, 7, 8, 8, 10] and target value 8,
    return [3, 4].
"""
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if nums is None or nums == []:
            return [-1, -1]
        if target < nums[0] or target > nums[-1]:
            return [-1, -1]
        lleft, lright = 0, len(nums) - 1
        rleft, rright = 0, len(nums) - 1
        while lleft < lright - 1:
            lmid = lleft + (lright - lleft) // 2
            if nums[lmid] >= target:
                lright = lmid
            else:
                lleft = lmid
        if nums[lleft] == target:
            lloc = lleft
        elif nums[lright] == target:
            lloc = lright
        else:
            return [-1, -1]

        while rleft < rright - 1:
            rmid = rleft + (rright - rleft) // 2
            if nums[rmid] <= target:
                rleft = rmid
            else:
                rright = rmid
        if nums[rright] == target:
            rloc = rright
        else:
            rloc = rleft
        return [lloc, rloc]

a = Solution()
print(a.searchRange([1, 2, 3], 1))
print(a.searchRange([5, 7, 7, 8, 8, 10], 8))
print(a.searchRange([2, 2], 2))
print(a.searchRange([1, 5], 4))
