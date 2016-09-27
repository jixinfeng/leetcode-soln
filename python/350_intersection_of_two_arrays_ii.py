"""
Given two arrays, write a function to compute their intersection.

Example:
    Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2, 2].

Note:
    Each element in the result should appear as many times as it shows in
    both arrays.
    The result can be in any order.

Follow up:
    What if the given array is already sorted? How would you optimize
    your algorithm?
    What if nums1's size is small compared to num2's size? Which
    algorithm is better?
    What if elements of nums2 are stored on disk, and the memory is
    limited such that you cannot load all elements into the memory at
    once?
"""
class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        if len(nums1)==0 or len(nums2)==0:
            return []
        count1={}
        for num in nums1:
            count1[num]=count1.get(num,0)+1
        count2={}
        for num in nums2:
            count2[num]=count2.get(num,0)+1
        inter=[]
        for num in count1.keys():
            if num in count2:
                for i in range(min(count1[num],count2[num])):
                    inter.append(num)
        return inter

"""
double pointer solution from:
http://bookshadow.com/weblog/2016/05/21/leetcode-intersection-of-two-arrays-ii/

def intersect(self, nums1, nums2):
    nums1, nums2 = sorted(nums1), sorted(nums2)
    p1 = p2 = 0
    ans = []
    while p1 < len(nums1) and p2 < len(nums2):
        if nums1[p1] < nums2[p2]:
            p1 += 1
        elif nums1[p1] > nums2[p2]:
            p2 += 1
        else:
            ans += nums1[p1],
            p1 += 1
            p2 += 1
    return ans
"""
