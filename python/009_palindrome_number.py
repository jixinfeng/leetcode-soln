"""
Determine whether an integer is a palindrome. Do this without extra space.

Some hints:
    Could negative integers be palindromes? (ie, -1)
    
    If you are thinking of converting the integer to string, note the
    restriction of using extra space.
    
    You could also try reversing an integer. However, if you have solved the
    problem "Reverse Integer", you know that the reversed integer might
    overflow. How would you handle such case?
    
    There is a more generic way of solving this problem.
"""
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        elif x < 10:
            return True
        elif x % 10 == 0:
            return False
        revx = 0
        tmpx = x
        while tmpx > 0:
            revx = revx * 10 + tmpx % 10
            tmpx //= 10
        return revx == x

a = Solution()
print(a.isPalindrome(-1) == False)
print(a.isPalindrome(1) == True)
print(a.isPalindrome(121) == True)
print(a.isPalindrome(1221) == True)
print(a.isPalindrome(10021) == False)
