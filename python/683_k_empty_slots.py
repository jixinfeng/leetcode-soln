"""
There is a garden with N slots. In each slot, there is a flower. The N flowers
will bloom one by one in N days. In each day, there will be exactly one flower
blooming and it will be in the status of blooming since then.

Given an array flowers consists of number from 1 to N. Each number in the array
represents the place where the flower will open in that day.

For example, flowers[i] = x means that the unique flower that blooms at day i
will be at position x, where i and x will be in the range from 1 to N.

Also given an integer k, you need to output in which day there exists two
flowers in the status of blooming, and also the number of flowers between them
is k and these flowers are not blooming.

If there isn't such day, output -1.

Example 1:
Input: 
flowers: [1,3,2]
k: 1
Output: 2
Explanation: In the second day, the first and the third flower have become
blooming.

Example 2:
Input: 
flowers: [1,2,3]
k: 1
Output: -1

Note:
The given array will be in the range [1, 20000].
"""
class Solution(object):
    def kEmptySlots(self, flowers, k):
        """
        :type flowers: List[int]
        :type k: int
        :rtype: int
        """
        if len(flowers) < 2:
            return -1
        bloomed = sorted([flowers[0], flowers[1]])
        if bloomed[1] - bloomed[0] - 1 == k:
            return 2
        
        for i in range(2, len(flowers)):
            curr_day = i + 1
            if flowers[i] < bloomed[0]:
                bloomed.insert(0, flowers[i])
                if bloomed[1] - bloomed[0] - 1 == k:
                    return curr_day
            elif flowers[i] > bloomed[-1]:
                bloomed.append(flowers[i])
                if bloomed[-1] - bloomed[-2] - 1 == k:
                    return curr_day
            else:
                j = self.binary_search(bloomed, flowers[i])
                bloomed.insert(j, flowers[i])
                if bloomed[j] - bloomed[j - 1] - 1 == k or \
                   bloomed[j + 1] - bloomed[j] - 1 == k:
                    return curr_day
                else:
                    continue
        return -1

    def binary_search(self, bloomed, entry):
        begin, end = 0, len(bloomed)
        while end > begin + 1:
            mid = (begin + end) // 2
            if entry > bloomed[mid]:
                begin = mid
            else:
                end = mid
        return end

a = Solution()
assert a.kEmptySlots([1, 3, 2], 1) == 2
assert a.kEmptySlots([1, 2, 3, 4], 1) == -1
assert a.kEmptySlots([6,5,8,9,7,1,10,2,3,4], 2) == 8
