"""
The count-and-say sequence is the sequence of integers beginning as follows:
    1, 11, 21, 1211, 111221, ...

1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.
Given an integer n, generate the nth sequence.

Note: The sequence of integers will be represented as a string.
"""
class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n==0:
            return 0
        for i in range(1,n+1):
            if i==1:
                nums=[1]
            else:
                digit=nums[0]
                count=0
                newNums=[]
                for num in nums:
                    if num==digit:
                        count+=1
                    else:
                        newNums.append(count)
                        newNums.append(digit)
                        digit=num
                        count=1
                newNums.append(count)
                newNums.append(digit)
                nums=newNums
        s=[str(c) for c in nums]
        return ''.join(s)

a=Solution()
for i in range(1,10):
    print(i,a.countAndSay(i))
