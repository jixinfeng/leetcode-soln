"""
Given an array of integers that is already sorted in ascending order, find two
numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add
up to the target, where index1 must be less than index2. Please note that your
returned answers (both index1 and index2) are not zero-based.

You may assume that each input would have exactly one solution.

Input: numbers={2, 7, 11, 15}, target=9
Output: index1=1, index2=2
"""
class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        l=len(numbers)
        for i in range(l):
            if i>0 and numbers[i]==numbers[i-1]:
                continue
            left,right=i,l
            while right>left+1:
                loc=(left+right)//2
                if numbers[i]+numbers[loc]>target:
                    right=loc
                elif numbers[i]+numbers[loc]<target:
                    left=loc
                elif numbers[i]+numbers[loc]==target:
                    return [i+1,loc+1]

a=Solution()
print(a.twoSum([2,7,11,15],18))
