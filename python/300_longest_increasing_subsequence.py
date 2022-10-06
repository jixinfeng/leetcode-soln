"""
Given an unsorted array of integers, find the length of longest increasing
subsequence.

For example,
Given [10, 9, 2, 5, 3, 7, 101, 18],
The longest increasing subsequence is [2, 3, 7, 101], therefore the length is 4.
Note that there may be more than one LIS combination, it is only necessary for
you to return the length.

Your algorithm should run in O(n2) complexity.

Follow up: Could you improve it to O(n log n) time complexity?

Credits:
    Special thanks to @pbrother for adding this problem and creating all test
    cases.
"""
import bisect


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0

        dp = []
        for i in range(len(nums)):
            if not dp or nums[i] > dp[-1]:
                dp.append(nums[i])
            else:
                j = bisect.bisect_left(dp, nums[i])
                dp[j] = nums[i]

        return len(dp)


a = Solution()
print(a.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]))

"""
DP solution O(n^2)
    def lengthOfLIS(self, nums):
        if nums is None or nums == []:
            return 0
        lenSubSeq = [1 for i in range(len(nums))]
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    lenSubSeq[i] = max(lenSubSeq[i], lenSubSeq[j] + 1)
        return max(lenSubSeq)
"""
