class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        Note:
        Dynamic Programming
        
        dp[i]=max(dp[i-2]+num[i],dp[i-1])
        dp[0]=nums[0]
        dp[1]=max(nums[0],nums[1])

    	Shorter Approach:
        a=0
        b=0
        for num in nums:
            m=a
            n=b
            a=n+num
            b=max(m,n)
        return max(a,b)
        """
        l = len(nums)
        if l == 0:
            return 0
        elif l == 1:
            return nums[0]
        elif l == 2:
            return max(nums)

        dp=[0] * l
        for i in range(l):
            if i == 0:
                dp[0] = nums[0]
            elif i == 1:
                dp[1] = max(nums[0], nums[1])
            else:
                dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])
        return dp[-1]
