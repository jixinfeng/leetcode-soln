"""
Given a non-empty integer array of size n, find the minimum number of moves
required to make all array elements equal, where a move is incrementing n - 1
elements by 1.

Example:

Input:
[1,2,3]

Output:
3

Explanation:
Only three moves are needed (remember each move increments two elements):

[1,2,3]  =>  [2,3,3]  =>  [3,4,3]  =>  [4,4,4]
"""
class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sum(nums) - len(nums) * min(nums)

assert Solution().minMoves([1,2,3]) == 3
print('pass')

"""
Note:
    Math problem, add 1 to n - 1 elements is equivalent to add 1 to all elements
    and substract 1 from 1 element.  Adding 1 to all element doesn't change the
    equality property, so the problem become finding out the number of steps
    needed to make all element equal by substract 1 from 1 element at each step
"""
