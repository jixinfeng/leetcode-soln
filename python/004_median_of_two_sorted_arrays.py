"""
There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should
be O(log (m+n)).

Example 1:
    nums1 = [1, 3]
    nums2 = [2]

    The median is 2.0

Example 2:
    nums1 = [1, 2]
    nums2 = [3, 4]

    The median is (2 + 3)/2 = 2.5
"""
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        length = len(nums1) + len(nums2)
        if length % 2 == 1:
            return self.findKthSmall(nums1, nums2, length // 2 + 1)
        else:
            small = self.findKthSmall(nums1, nums2, length // 2)
            big = self.findKthSmall(nums1, nums2, length // 2 + 1)
            return (small + big) / 2.0

    def findKthSmall(self, nums1, nums2, k):
        if len(nums1) == 0:
            return nums2[k - 1]
        if len(nums2) == 0:
            return nums1[k - 1]
        if k == 1:
            return min(nums1[0], nums2[0])
        num1 = nums1[k // 2 - 1] if len(nums1) >= k // 2 else None
        num2 = nums2[k // 2 - 1] if len(nums2) >= k // 2 else None
        if num2 is None or (num1 is not None and num1 < num2):
            return self.findKthSmall(nums1[k // 2:], nums2, k - k // 2)
        else:
            return self.findKthSmall(nums1, nums2[k // 2:], k - k // 2)

a = Solution()
print(a.findMedianSortedArrays([1,3],[2]) == 2)
print(a.findMedianSortedArrays([1,3],[2,4]) == 2.5)
print(a.findMedianSortedArrays([1,3,5],[2,4]) == 3)
