"""
Given a non-empty array of integers, return the k most frequent elements.

For example,
Given [1,1,1,2,2,3] and k = 2, return [1,2].

Note: 
    You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
    Your algorithm's time complexity must be better than O(n log n), where n is
    the array's size.
"""
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if not nums or not k:
            return []
        if len(nums) < k:
            return []
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
            
        freq = []
        heapq.heapify(freq)
        for i, j in count.items():
            heapq.heappush(freq, (-j, i))
        soln = []
        for i in range(k):
            soln.append(heapq.heappop(freq)[1])
        return soln
