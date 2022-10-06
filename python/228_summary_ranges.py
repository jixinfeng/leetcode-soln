"""
Given a sorted integer array without duplicates, return the summary of its
ranges.

For example, given [0,1,2,4,5,7], return ["0->2","4->5","7"].

Credits:
Special thanks to @jianchao.li.fighter for adding this problem and creating all
test cases.
"""


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []

        ranges = []
        curr_range = []
        for i in range(len(nums) - 1):
            if not curr_range:
                curr_range.append(nums[i])

            if nums[i + 1] - nums[i] > 1:
                curr_range.append(nums[i])
                ranges.append(sorted(set(curr_range)))
                curr_range = []

        if not curr_range:
            ranges.append([nums[-1]])
        else:
            curr_range.append(nums[-1])
            ranges.append(sorted(set(curr_range)))

        solution = ['->'.join(map(str, r)) for r in ranges]

        return solution


a = Solution()
print(a.summaryRanges([0, 1, 2, 4, 5, 7, 8, 9]))
