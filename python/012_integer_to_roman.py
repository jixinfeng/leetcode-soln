"""
Given an integer, convert it to a roman numeral.

Input is guaranteed to be within the range from 1 to 3999.
"""
class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num is None or num == 0:
            return ""
        integers = [1000, 100, 10, 1]
        romans = [['M'], ['C', 'D'], ['X', 'L'], ['I', 'V']]
        roman = []
        for i, j in enumerate(integers):
            if num < j:
                continue
            digit = num // j
            if digit < 4:
                for k in range(digit):
                    roman.append(romans[i][0])
            elif digit == 4:
                roman.append(romans[i][0])
                roman.append(romans[i][1])
            elif digit < 9:
                roman.append(romans[i][1])
                for k in range(digit - 5):
                    roman.append(romans[i][0])
            else:
                roman.append(romans[i][0])
                roman.append(romans[i - 1][0])
            num %= j
        return ''.join(roman)

a = Solution()
nums = [0,1,2,3,4,5,6,7,8,9,10,20,30,40,50,60,90,100,3999]
for i in nums:
    print(i,a.intToRoman(i))
