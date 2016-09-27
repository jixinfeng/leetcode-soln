"""
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one
sorted array.

Note:
    You may assume that nums1 has enough space (size that is greater or equal to
    m + n) to hold additional elements from nums2. The number of elements
    initialized in nums1 and nums2 are m and n respectively.
"""
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        if len(nums1)>m:
            for i in range(m,len(nums1)):
                nums1.pop()
        if len(nums2)>n:
            for i in range(n,len(nums2)):
                nums2.pop()
        p=0
        while len(nums2)>0:
            if len(nums1)==0 or nums1[p]>nums2[0]:
                nums1.insert(p,nums2[0])
                del nums2[0]
                if p<len(nums1)-1:
                    p+=1
            else:
                if p<len(nums1)-1:
                    p+=1
                else:
                    nums1.append(nums2[0])
                    del nums2[0]
