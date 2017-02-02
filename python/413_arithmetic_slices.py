"""
A sequence of number is called arithmetic if it consists of at least three
elements and if the difference between any two consecutive elements is the same.

For example, these are arithmetic sequence:

    1, 3, 5, 7, 9
    7, 7, 7, 7
    3, -1, -5, -9

The following sequence is not arithmetic.

    1, 1, 2, 5, 7

A zero-indexed array A consisting of N numbers is given. A slice of that array
is any pair of integers (P, Q) such that 0 <= P < Q < N.

A slice (P, Q) of array A is called arithmetic if the sequence:
A[P], A[p + 1], ..., A[Q - 1], A[Q] is arithmetic. In particular, this means
that P + 1 < Q.

The function should return the number of arithmetic slices in the array A.


Example:

    A = [1, 2, 3, 4]

return: 3, for 3 arithmetic slices in A: [1, 2, 3], [2, 3, 4] and [1, 2, 3, 4]
itself.
"""
class Solution(object):
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if len(A) < 3:
            return 0
        soln = 0
        start, end = 0, 0
        while start < len(A) - 2:
            end = start + 1
            delta = A[end] - A[start]
            while end < len(A) - 1 and A[end + 1] - A[end] == delta:
                end += 1
            soln += (end - start - 1) * (end - start) // 2
            start = end
        return soln

assert Solution().numberOfArithmeticSlices([]) == 0
assert Solution().numberOfArithmeticSlices([1]) == 0
assert Solution().numberOfArithmeticSlices([1,1,1]) == 1
assert Solution().numberOfArithmeticSlices([1,3,5,7,9]) == 6
assert Solution().numberOfArithmeticSlices([7,7,7,7]) == 3
assert Solution().numberOfArithmeticSlices([1,1,2,5,7]) == 0
assert Solution().numberOfArithmeticSlices([1,2,3,4]) == 3
assert Solution().numberOfArithmeticSlices([1,3,5,7,9,20,2,4,6,8,10]) == 12
print('pass')
