"""
You are given two jugs with capacities x and y litres. There is an infinite
amount of water supply available. You need to determine whether it is possible
to measure exactly z litres using these two jugs.

If z liters of water is measurable, you must have z liters of water contained
within one or both buckets by the end.

Operations allowed:

Fill any of the jugs completely with water.
Empty any of the jugs.
Pour water from one jug into another till the other jug is completely full or
the first jug itself is empty.
Example 1: (From the famous "Die Hard" example)

    Input: x = 3, y = 5, z = 4
    Output: True

Example 2:

    Input: x = 2, y = 6, z = 5
    Output: False
Credits:
    Special thanks to @vinod23 for adding this problem and creating all test
    cases.
"""
class Solution(object):
    def canMeasureWater(self, x, y, z):
        """
        :type x: int
        :type y: int
        :type z: int
        :rtype: bool
        """
        if z == 0:
            return True
        if z > x + y:
            return False
        w = self.gcd(x, y)
        return z % w == 0

    def gcd(self, a, b):
        if b == 0:
            return a
        else:
            return self.gcd(b, a % b)

a = Solution()
print(a.canMeasureWater(3, 5, 4))
print(a.canMeasureWater(2, 6, 5))
