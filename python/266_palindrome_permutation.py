"""
Given a string, determine if a permutation of the string could form a
palindrome.

For example,
"code" -> False, "aab" -> True, "carerac" -> True.

Hint:

    Consider the palindromes of odd vs even length. What difference do you
    notice?
    Count the frequency of each character.
    If each character occurs even number of times, then it must be a palindrome.
    How about character which occurs odd number of times?
"""
class Solution(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s)<=1:
            return True
        cCount={}
        for c in s:
            cCount[c]=cCount.get(c,0)+1
        fOdds=0
        for f in cCount.values():
            if f%2==1:
                fOdds+=1
                if fOdds>1:
                    return False
        return True
