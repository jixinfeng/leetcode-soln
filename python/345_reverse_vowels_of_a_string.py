"""
Write a function that takes a string as input and reverse only the vowels of a
string.

Example 1:
    Given s = "hello", return "holle".

Example 2:
    Given s = "leetcode", return "leotcede".
"""
class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s)<=1:
            return s
        vowels=set(['a','e','i','o','u'])
        word=[c for c in s]
        left,right=0,len(s)-1
        while left<=right:
            while left<len(s) and word[left].lower() not in vowels:
                left+=1
            while right>=0 and word[right].lower() not in vowels:
                right-=1
            if left>=right:
                break
            word[left],word[right]=word[right],word[left]
            left,right=left+1,right-1
        return ''.join(word)

"""
Solution using regex:
def reverseVowels(self, s):
    vowels = re.findall('(?i)[aeiou]', s)
    return re.sub('(?i)[aeiou]', lambda m: vowels.pop(), s)
"""
