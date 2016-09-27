"""
Compare two version numbers version1 and version2.
If version1 > version2 return 1, if version1 < version2 return -1, otherwise
return 0.

You may assume that the version strings are non-empty and contain only digits
and the . character.
The . character does not represent a decimal point and is used to separate
number sequences.
For instance, 2.5 is not "two and a half" or "half way to version three", it is
the fifth second-level revision of the second first-level revision.

Here is an example of version numbers ordering:

    0.1 < 1.1 < 1.2 < 13.37

Credits:
    Special thanks to @ts for adding this problem and creating all test
    cases.
"""
class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        array1=version1.split('.')
        array1=[int(c) for c in array1]
        while len(array1)>0 and array1[-1]==0:
            array1.pop()
        array2=version2.split('.')
        array2=[int(c) for c in array2]
        while len(array2)>0 and array2[-1]==0:
            array2.pop()
        l1=len(array1)
        l2=len(array2)
        for i in range(min(l1,l2)):
            if array1[i]<array2[i]:
                return -1
            elif array1[i]>array2[i]:
                return 1
        if l1>l2:
            return 1
        elif l1==l2:
            return 0
        else:
            return -1

