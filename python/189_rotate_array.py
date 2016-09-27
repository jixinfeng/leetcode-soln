"""
Rotate an array of n elements to the right by k steps.

For example, with n = 7 and k = 3, the array [1,2,3,4,5,6,7] is rotated to
[5,6,7,1,2,3,4].

Note:
    Try to come up as many solutions as you can, there are at least 3 different
    ways to solve this problem.

Hint:
    Could you do it in-place with O(1) extra space?

    Related problem: Reverse Words in a String II

Credits:
    Special thanks to @Freezen for adding this problem and creating all test
    cases.

    Show Company Tags
    Show Tags
    Show Similar Problems
"""
class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        k%=n
        nums[:]=nums[n-k:]+nums[:n-k]

"""
Note:

    def rotate(self, nums, k):
        n = len(nums)
        k %= n
        self.reverse(nums, 0, n - k)
        self.reverse(nums, n - k, n)
        self.reverse(nums, 0, n)

    def reverse(self, nums, start, end):
        for x in range(start, (start + end) / 2):
            nums[x] ^= nums[start + end - x - 1]
            nums[start + end - x - 1] ^= nums[x]
            nums[x] ^= nums[start + end - x - 1]
"""
