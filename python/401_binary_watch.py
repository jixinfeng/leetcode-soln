"""
A binary watch has 4 LEDs on the top which represent the hours (0-11), and the 6
LEDs on the bottom represent the minutes (0-59).

Each LED represents a zero or one, with the least significant bit on the right.

![Binary Watch 3:25](https://upload.wikimedia.org/wikipedia/commons/8/8b/Binary_clock_samui_moon.jpg)

For example, the above binary watch reads "3:25".

Given a non-negative integer n which represents the number of LEDs that are
currently on, return all possible times the watch could represent.

Example:

Input: n = 1
    Return: ["1:00", "2:00", "4:00", "8:00", "0:01", "0:02", "0:04", "0:08", "0:16", "0:32"]
Note:
    The order of output does not matter.

    The hour must not contain a leading zero, for example "01:00" is not valid,
    it should be "1:00".

    The minute must be consist of two digits and may contain a leading zero, for
    example "10:2" is not valid, it should be "10:02".
"""
class Solution(object):
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        if num > 10 or num < 0:
            return []
        soln = []
        for comb in itertools.combinations(range(10), num):
            h = int("".join(['1' if i in comb 
                             else '0'
                             for i in range(4)]), 2)
            m = int("".join(['1' if i in comb 
                             else '0'
                             for i in range(4, 10)]), 2)
            if h < 12 and m < 60:
                soln.append(str(h) + ":" + str(m).zfill(2))
        return soln

import itertools
a = Solution()
print(a.readBinaryWatch(1))
