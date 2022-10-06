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


class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        char_count = {}
        for c in s:
            char_count[c] = char_count.get(c, 0) + 1

        odd_count = 0
        for count in char_count.values():
            if count % 2:
                odd_count += 1

        return (len(s) % 2 == 0 and odd_count == 0) or (len(s) % 2 == 1 and odd_count == 1)
