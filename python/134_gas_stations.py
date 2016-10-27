"""
There are N gas stations along a circular route, where the amount of gas at
station i is gas[i].

You have a car with an unlimited gas tank and it costs cost[i] of gas to travel
from station i to its next station (i+1). You begin the journey with an empty
tank at one of the gas stations.

Return the starting gas station's index if you can travel around the circuit
once, otherwise return -1.

Note:
    The solution is guaranteed to be unique.
"""
class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        start, gasLeft = 0, 0
        for i in range(len(gas)):
            gasLeft += gas[i] - cost[i]
            if gasLeft < 0:
                start += i + 1
                gasLeft = 0
        return start if sum(gas) >= sum(cost) else -1

import collections
a = Solution()
print(a.canCompleteCircuit([1,2,3,4,5],[3,3,3,3,3]))
