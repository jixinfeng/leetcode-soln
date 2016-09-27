"""
Given a sorted integer array without duplicates, return the summary of its
ranges.

For example, given [0,1,2,4,5,7], return ["0->2","4->5","7"].

Credits:
Special thanks to @jianchao.li.fighter for adding this problem and creating all
test cases.
"""
class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if nums is None or nums == []:
            return []
        if len(nums) == 1:
            return [str(nums[0])]
        soln = []
        lower, upper = nums[0], nums[0]
        for i in range(len(nums) - 1):
            if nums[i] + 1 == nums[i + 1]:
                continue
            else:
                upper = nums[i]
                if upper > lower:
                    soln.append(str(lower) + '->' + str(upper))
                else:
                    soln.append(str(upper))
                lower = nums[i + 1]
        upper = nums[-1]
        if upper > lower:
            soln.append(str(lower) + '->' + str(upper))
        else:
            soln.append(str(upper))
        return soln

a = Solution()
print(a.summaryRanges([0,1,2,4,5,7,8,9]))
