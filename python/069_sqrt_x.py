"""
Implement int sqrt(int x).

Compute and return the square root of x.
"""
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """ 
        if x < 0:
            return None
        elif x <= 1:
            return x
        low, high = 0, x - 1
        while low + 1 < high:
            mid = low + (high - low) // 2
            trial = mid ** 2
            if trial == x:
                return mid
            elif trial < x:
                low = mid
            else:
                high = mid
        return high if high ** 2 <= x else low

a = Solution()
for i in range(17):
    print(a.mySqrt(i))

"""
    def mySqrt(self, x):
        if x < 0:
            return None
        elif x <= 1:
            return x
        elif x == 2:
            return 1
        xo, xn = x, x - 2
        while xo > xn + 1:
            xo = xn
            xn = int((xo + x / xo) / 2)
        return xn if xn ** 2 <= x else xn - 1
"""
