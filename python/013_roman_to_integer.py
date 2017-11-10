"""
Given a roman numeral, convert it to an integer.

Input is guaranteed to be within the range from 1 to 3999.
"""
class Solution(object):
    romans = {'I' : 1,
              'V' : 5,
              'X' : 10,
              'L' : 50,
              'C' : 100,
              'D' : 500,
              'M' : 1000}
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        rlen = len(s)
        if rlen == 0:
            return 0
        intlst = []
        for i in range(rlen):
            intlst.append(self.romans[s[i]])
        if rlen == 1:
            return intlst[0]
        num = 0
        for i in range(rlen):
            if i == 0:
                num += intlst[0]
                continue
            if intlst[i] <= intlst[i-1]:
                num += intlst[i]
            else:
                num += intlst[i] - 2 * intlst[i - 1]
        return num

a=Solution()
roman=['X','I','V']
print(a.romanToInt(roman))
