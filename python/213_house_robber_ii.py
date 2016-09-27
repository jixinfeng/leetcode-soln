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
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums is None or nums == []:
            return 0
        l = len(nums)
        if l == 1:
            return nums[0]
        if l == 2:
            return max(nums)
        solns = []
        for i in range(l):
            dp = [0] * l
            houses = nums[i:] + nums[:i]
            for i in range(l):
                if i == 0:
                    dp[0] = houses[0]
                elif i == 1:
                    dp[1] = max(houses[0], houses[1])
                elif i < l - 1:
                    dp[i] = max(dp[i - 2] + houses[i], dp[i - 1])
                else:
                    dp[i] = max(dp[i - 2] + houses[i], dp[i - 1]) \
                            if dp[0] == 0 else 0
            solns.append(max(dp[-2],dp[-1]))
        return max(solns)

a = Solution()
print(a.rob([1,2,3,4,5]) == 8)
print(a.rob([1,3,5,7,9,2,4,6,8,10]) == 30)
