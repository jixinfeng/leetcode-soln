"""
Given a non negative integer number num. For every numbers i in the range 0 ≤ i
≤ num calculate the number of 1's in their binary representation and return them
as an array.

Example:
    For num = 5 you should return [0,1,1,2,1,2].

Follow up:
    It is very easy to come up with a solution with run time
    O(n*sizeof(integer)). But can you do it in linear time O(n) /possibly in
    a single pass?
    Space complexity should be O(n).
    Can you do it like a boss? Do it without using any builtin function like
    __builtin_popcount in c++ or in any other language.

Hint:
    You should make use of what you have produced already.
    Divide the numbers in ranges like [2-3], [4-7], [8-15] and so on.
    And try to generate new range from previous.
    Or does the odd/even status of the number help you in calculating
    the number of 1s?

Credits:
    Special thanks to @ syedee for adding this problem and creating
    all test cases.
"""
class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        numBits=[0]
        nearestPowOfTwo=lambda x: 2**int(math.log(x,2))
        for i in range(1,num+1):
#            numBits.append(numBits[i//2]+(i&1))
            numBits.append(numBits[i-nearestPowOfTwo(i)]+1)
        return numBits


import math
a=Solution()
print(a.countBits(5))

"""
Note: Number of 1s in bin(i) is equal to number of 1s in tail bits of it plus 1

    def countBits(self, num):
        numBits=[0]
        nearestPowOfTwo=lambda x: 2**int(math.log(x,2))
        currentPowOfTwo=1
        for i in range(1,num+1):
            if i>=currentPowOfTwo*2:
                currentPowOfTwo=nearestPowOfTwo(i)
            numBits.append(numBits[i-currentPowOfTwo]+1)
        return numBits
"""
