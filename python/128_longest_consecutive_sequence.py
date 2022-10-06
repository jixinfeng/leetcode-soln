"""
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9

Constraints:

0 <= nums.length <= 105
-109 <= nums[i] <= 109
"""


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        longest_consecutive = 0

        nums_set = set(nums)
        for n in nums:
            if n in nums_set:
                curr_consecutive = 1
                nums_set.remove(n)
                prev_n = n - 1
                next_n = n + 1
                while prev_n in nums_set:
                    nums_set.remove(prev_n)
                    curr_consecutive += 1
                    prev_n -= 1

                while next_n in nums_set:
                    nums_set.remove(next_n)
                    curr_consecutive += 1
                    next_n += 1

                longest_consecutive = max(longest_consecutive, curr_consecutive)

        return longest_consecutive
