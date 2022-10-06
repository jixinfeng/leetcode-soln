"""
Given a non-negative integer num, repeatedly add all its digits until the result
has only one digit.

For example:

    Given num = 38, the process is like: 3 + 8 = 11, 1 + 1 = 2. Since 2 has only
    one digit, return it.

Follow up:
    Could you do it without any loop/recursion in O(1) runtime?

Hint:
    A naive implementation of the above process is trivial. Could you
    come up with other methods?
    What are all the possible results?
    How do they occur, periodically or randomly?
    You may find this Wikipedia article useful.

Credits:
    Special thanks to @jianchao.li.fighter for adding this problem
    and creating all test cases.
"""


class Solution:
    def addDigits(self, num: int) -> int:
        while num >= 10:
            c = 0
            while num:
                num, r = divmod(num, 10)
                c += r
            num = c
        return num


# class Solution:
#     def addDigits(self, num: int) -> int:
#         while num >= 10:
#             num = sum(map(int, list(str(num))))
#         return num
