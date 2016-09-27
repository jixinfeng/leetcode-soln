"""
Given a sorted array of integers nums and integer values a, b and c. Apply a
function of the form f(x) = ax2 + bx + c to each element x in the array.

The returned array must be in sorted order.

Expected time complexity: O(n)

Example:

    nums = [-4, -2, 2, 4], a = 1, b = 3, c = 5,

    Result: [3, 9, 15, 33]

    nums = [-4, -2, 2, 4], a = -1, b = 3, c = 5

    Result: [-23, -5, 1, 7]

Credits:
    Special thanks to @elmirap for adding this problem and creating all test cases.
"""
class Solution(object):
    def sortTransformedArray(self, nums, a, b, c):
        """
        :type nums: List[int]
        :type a: int
        :type b: int
        :type c: int
        :rtype: List[int]
        """
        if nums is None or nums == []:
            return []
        length = len(nums)
        if length == 1:
            x = nums[0]
            return [a * x * x + b * x + c]
        quad = [a * x ** 2 + b * x + c for x in nums]
        soln = [0 for i in range(length)]
        left, right = 0, length - 1
        if a >= 0:
            loc = length - 1
            while left < right - 1:
                if quad[left] >= quad[right]:
                    soln[loc] = quad[left]
                    left += 1
                else:
                    soln[loc] = quad[right]
                    right -= 1
                loc -= 1
            if quad[left] >= quad[right]:
                soln[loc] = quad[left]
                soln[loc - 1] = quad[right]
            else:
                soln[loc] = quad[right]
                soln[loc - 1] = quad[left]
        else:
            loc = 0
            while left < right - 1:
                if quad[left] <= quad[right]:
                    soln[loc] = quad[left]
                    left += 1
                else:
                    soln[loc] = quad[right]
                    right -= 1
                loc += 1
            if quad[left] <= quad[right]:
                soln[loc] = quad[left]
                soln[loc + 1] = quad[right]
            else:
                soln[loc] = quad[right]
                soln[loc + 1] = quad[left]
        return soln
