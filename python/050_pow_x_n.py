"""
Implement pow(x, n).
"""
class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n < 0:
            if x == 0:
                return None
            else:
                return 1 / self.myPow(x, -1 * n)
        elif n == 0:
            if x == 0:
                return None
            else:
                return 1
        elif n == 1:
            return x
        elif n % 2:
            return self.myPow(x * x, n // 2) * x
        else:
            return self.myPow(x * x, n // 2)

a = Solution()
for i in range(17):
    print(a.myPow(2,i))

for j in range(4):
    print(a.myPow(2,-j))
