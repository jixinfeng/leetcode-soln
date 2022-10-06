"""
Note: This is an extension of House Robber.

After robbing those houses on that street, the thief has found himself a new
place for his thievery so that he will not get too much attention. This time,
all houses at this place are arranged in a circle. That means the first house is
the neighbor of the last one. Meanwhile, the security system for these houses
remain the same as for those in the previous street.

Given a list of non-negative integers representing the amount of money of each
house, determine the maximum amount of money you can rob tonight without
alerting the police.

Credits:
    Special thanks to @Freezen for adding this problem and creating all test
    cases.
"""


class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) <= 2:
            return max(nums)

        return max(self.rob_i(nums[:-1]), self.rob_i(nums[1:]))

    def rob_i(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[:2])
        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])

        return dp[-1]


a = Solution()
print(a.rob([1, 2, 3, 4, 5]) == 8)
print(a.rob([1, 3, 5, 7, 9, 2, 4, 6, 8, 10]) == 30)
