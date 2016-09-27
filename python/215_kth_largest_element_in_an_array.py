"""
Find the kth largest element in an unsorted array. Note that it is the kth
largest element in the sorted order, not the kth distinct element.

For example,
    Given [3,2,1,5,6,4] and k = 2, return 5.

Note: 
    You may assume k is always valid, 1 ≤ k ≤ array's length.

Credits:
    Special thanks to @mithmatt for adding this problem and creating all test
    cases.
"""
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if nums is None or nums == []:
            return None
        if k == 1:
            return max(nums)
        if k == len(nums):
            return min(nums)
        if k < 0 or k > len(nums):
            return None
        left, pvt, right = self.partition(nums)
        if len(right) == k - 1:
            return pvt
        elif len(right) > k - 1:
            return self.findKthLargest(right, k)
        else:
            return self.findKthLargest(left, k - len(right) - 1)

    def partition(self, nums):
        if len(nums) == 1:
            return [], nums, []
        elif len(nums) == 2:
            if nums[0] <= nums[1]:
                return [], nums[0], [nums[1]]
            else:
                return [], nums[1], [nums[0]]
        left, right = [], []
        pIdx = random.randint(0, len(nums) - 1)
        pvt = nums[pIdx]
        for i, j in enumerate(nums):
            if i != pIdx:
                if j < pvt:
                    left.append(j)
                else:
                    right.append(j)
        return (left, pvt, right)

import random
import heapq
a = Solution()
passed = True
for i in range(10):
    testList = [random.randint(1, 100) for i in range(100)]
    testLoc = random.randint(1, 100)
    QSsoln = a.findKthLargest(testList, testLoc)
    HPsoln = heapq.nlargest(testLoc, testList)[-1]
    if QSsoln != HPsoln:
        passed = False
        break
    
print('pass' if passed else 'failed')



"""
Note:
    One-liner using heapq:

    def findKthLargest(self, nums, k):
        if nums is None or nums == []:
            return None
        return heapq.nlargest(k, nums)[-1]
"""
