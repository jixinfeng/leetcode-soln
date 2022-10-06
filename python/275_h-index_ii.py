"""
Follow up for H-Index: What if the citations array is sorted in ascending order?
Could you optimize your algorithm.

Hint:
    Expected runtime complexity is in O(log n) and the input is sorted.
"""


class Solution(object):
    def hIndex(self, citations: List[int]) -> int:
        """
        :type citations: List[int]
        :rtype: int
        """
        if citations is None or citations == []:
            return 0
        left, right = 0, len(citations) - 1
        while left < right:
            mid = left + (right - left) // 2
            if citations[mid] >= len(citations) - mid:
                right = mid
            else:
                left = mid + 1
        if citations[left] >= len(citations) - left:
            return len(citations) - left
        else:
            return 0


a = Solution()
print(a.hIndex([0]) == 0)
print(a.hIndex([1]) == 1)
print(a.hIndex([0, 1]) == 1)
print(a.hIndex([11, 15]) == 2)
