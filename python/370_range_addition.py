"""
Assume you have an array of length n initialized with all 0's and are given k
update operations.

Each operation is represented as a triplet: [startIndex, endIndex, inc] which
increments each element of subarray A[startIndex ... endIndex] (startIndex and
endIndex inclusive) with inc.

Return the modified array after all k operations were executed.

Example:
    Given:
    
        length = 5,
        updates = [
            [1,  3,  2],
            [2,  4,  3],
            [0,  2, -2]
        ]
    
    Output:
    
        [-2, 0, 3, 5, 3]

Explanation:
    Initial state:
    [ 0, 0, 0, 0, 0 ]
    
    After applying operation [1, 3, 2]:
    [ 0, 2, 2, 2, 0 ]
    
    After applying operation [2, 4, 3]:
    [ 0, 2, 5, 5, 3 ]
    
    After applying operation [0, 2, -2]:
    [-2, 0, 3, 5, 3 ]

Hint:
    Thinking of using advanced data structures? You are thinking it too complicated.

    For each update operation, do you really need to update all elements between i and j?

    Update only the first and end element is sufficient.

    The optimal time complexity is O(k + n) and uses O(1) extra space.

Credits:
    Special thanks to @vinod23 for adding this problem and creating all test cases.
"""
class Solution(object):
    def getModifiedArray(self, length, updates):
        """
        :type length: int
        :type updates: List[List[int]]
        :rtype: List[int]
        """
        soln = [0] * length
        mark = [0] * length
        for update in updates:
            mark[update[1]] += update[2]
            if update[0] > 0:
                mark[update[0] - 1] -= update[2]
        partialSum = 0
        for i in reversed(range(length)):
            partialSum += mark[i]
            soln[i] += partialSum
        return soln

a = Solution()
l = 5
u = [[1,3,2],[2,4,3],[0,2,-2]]
print(a.getModifiedArray(l, u))

"""
Note:
    https://discuss.leetcode.com/topic/49674/java-o-n-k-time-o-1-space-with-algorithm-explained
"""
