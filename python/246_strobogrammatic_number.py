"""
A strobogrammatic number is a number that looks the same when rotated 180
degrees (looked at upside down).

Write a function to determine if a number is strobogrammatic. The number is
represented as a string.

For example, the numbers "69", "88", and "818" are all strobogrammatic.
"""
class Solution(object):
    def isStrobogrammatic(self, num):
        """
        :type num: str
        :rtype: bool
        """
        original=[c for c in num]
        rev=original[:]
        rev.reverse()
        print(original)
        print(rev)
        for i in range(len(original)/2+1):
            if (original[i]=="6" and rev[i]=="9") or (original[i]=="9" and rev[i]=="6"):
                continue
            if original[i] in set(["0","1","8"]) and rev[i]==original[i]:
                continue
            else:
                return False
        return True

"""
Note:
    a=[1,2,3]
    b=a         #shallow copy
    c=a[:]      #deep copy
"""
