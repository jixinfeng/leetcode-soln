"""
Given a non-negative number represented as an array of digits, plus one to the
number.

The digits are stored such that the most significant digit is at the head of the
list.
"""
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        i=1
        carry=1
        while i<=len(digits):
            digit=(digits[-i]+carry)%10
            carry=(digits[-i]+carry)//10
            digits[-i]=digit
            if carry==0:
                break
            i+=1
        if carry==1:
            digits.insert(0,1)
        return digits
