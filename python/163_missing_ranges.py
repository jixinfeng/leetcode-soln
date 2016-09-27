"""
Given a sorted integer array where the range of elements are [lower, upper]
inclusive, return its missing ranges.

For example, given [0, 1, 3, 50, 75], lower = 0 and upper = 99, return ["2",
"4->49", "51->74", "76->99"].
"""
class Solution(object):
    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """
        if lower > upper:
            return []
        if nums is None or nums == []:
            if upper == lower:
                return [str(lower)]
            else:
                return [str(lower) + '->' + str(upper)]
        soln = []
        if lower < nums[0] - 1:
            soln.append(str(lower) + '->' + str(nums[0] - 1))
        elif lower == nums[0] - 1:
            soln.append(str(lower))
        for i in range(len(nums) - 1):
            if nums[i] >= upper:
                break
            elif nums[i + 1] == nums[i] + 1:
                continue
            elif nums[i + 1] == nums[i] + 2:
                soln.append(str(nums[i] + 1))
            else:
                soln.append(str(nums[i] + 1) + '->' + str(nums[i + 1] - 1))
        if nums[-1] < upper - 1:
            soln.append(str(nums[-1] + 1) + '->' + str(upper))
        elif nums[-1] == upper - 1:
            soln.append(str(upper))
        return soln

a = Solution()
print(a.findMissingRanges([0, 1, 3, 50, 75], 0, 99))
print(a.findMissingRanges([], 1, 1))
