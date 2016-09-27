"""
Find the contiguous subarray within an array (containing at least one number)
which has the largest sum.

For example, given the array [-2,1,-3,4,-1,2,1,-5,4],
the contiguous subarray [4,-1,2,1] has the largest sum = 6.

More practice:
If you have figured out the O(n) solution, try coding another solution using the
divide and conquer approach, which is more subtle.
"""
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums is None or nums == []:
            return 0
        if len(nums) == 1:
            return nums[0]
        sums = [0] * len(nums)
        sums[0] = nums[0]
        maxSum = nums[0]
        for i in range(1, len(nums)):
            sums[i] = nums[i] + max(sums[i - 1], 0)
            maxSum = max(maxSum, sums[i])
        return maxSum

a = Solution()
print(a.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
