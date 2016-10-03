"""
Implement atoi to convert a string to an integer.

Hint: Carefully consider all possible input cases. If you want a challenge,
please do not see below and ask yourself what are the possible input cases.

Notes: It is intended for this problem to be specified vaguely (ie, no given
input specs). You are responsible to gather all the input requirements up front.

Update (2015-02-10):
    The signature of the C++ function had been updated. If you still see your
    function signature accepts a const char * argument, please click the reload
    button to reset your code definition.
"""
class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        str = str.strip()
        match = re.findall('^([+-]?\d+).*$', str)
        if match == []:
            num = 0
        else:
            num = int(match[0])
        if num >= 2 ** 31:
            num = (2 ** 31) - 1
        elif num <- 2 ** 31:
            num =- 2 ** 31
        return num

import re
a=Solution()
cases = ['42','-42','3.14','3456 with words', '+-2',
       'words with 1234','2147483648','-2147483648']
matches = [42, -42, 3, 3456, 0,
           0, 2147483647, -2147483648]

for i in range(len(cases)):
    print('output of', "'", cases[i], "'", 'is', a.myAtoi(cases[i]))
    if a.myAtoi(cases[i]) == matches[i]:
        print('pass')
    else:
        print('not pass')
