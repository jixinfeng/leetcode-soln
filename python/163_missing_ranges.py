"""
Given a sorted integer array where the range of elements are [lower, upper]
inclusive, return its missing ranges.

For example, given [0, 1, 3, 50, 75], lower = 0 and upper = 99, return ["2",
"4->49", "51->74", "76->99"].
"""


class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        if not nums:
            ranges = [sorted({lower, upper})]
        else:
            ranges = []
            if nums[0] - lower > 0:
                ranges.append(sorted({lower, nums[0] - 1}))

            for i in range(len(nums) - 1):
                if nums[i + 1] - nums[i] > 1:
                    ranges.append(sorted({nums[i] + 1, nums[i + 1] - 1}))

            if upper - nums[-1] > 0:
                ranges.append(sorted({nums[-1] + 1, upper}))

        return list(map(lambda r: "->".join(map(str, r)), ranges))


a = Solution()
print(a.findMissingRanges([0, 1, 3, 50, 75], 0, 99))
print(a.findMissingRanges([], 1, 1))
print(a.findMissingRanges([-2147483648, -2147483648, 0, 2147483647, 2147483647], -2147483648, 2147483647))
