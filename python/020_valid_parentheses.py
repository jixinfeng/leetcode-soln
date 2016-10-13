"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid.

The brackets must close in the correct order, "()" and "()[]{}" are all valid
but "(]" and "([)]" are not."))"
"""
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        pstack = []
        pleft = set(['(', '[', '{'])
        for c in s:
            if c in pleft:
                pstack.append(c)
            elif c == ')':
                if pstack == [] or pstack.pop() != '(':
                    return False
            elif c == ']':
                if pstack == [] or pstack.pop() != '[':
                    return False
            elif c == '}':
                if pstack == [] or pstack.pop() != '{':
                    return False
        return len(pstack) == 0
