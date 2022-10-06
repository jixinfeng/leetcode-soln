"""
A strobogrammatic number is a number that looks the same when rotated 180
degrees (looked at upside down).

Write a function to determine if a number is strobogrammatic. The number is
represented as a string.

For example, the numbers "69", "88", and "818" are all strobogrammatic.
"""


class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        if len(num) == 1:
            return num in {'0', '1', '8'}
        if int(num) % 10 == 0:
            return False
        flip_dict = {'0': '0', '1': '1', '6': '9', '8': '8', '9': '6'}

        left, right = 0, len(num) - 1
        while left <= right:
            if left == right:
                return num[left] in {'0', '1', '8'}
            elif num[left] not in flip_dict or num[right] not in flip_dict:
                return False
            elif flip_dict[num[left]] != num[right]:
                return False
            else:
                left += 1
                right -= 1

        return True


"""
Note:
    a=[1,2,3]
    b=a         #shallow copy
    c=a[:]      #deep copy
"""
