"""
Given an array of numbers, verify whether it is the correct preorder traversal
sequence of a binary search tree.

You may assume each number in the sequence is unique.

Follow up:
Could you do it using only constant space complexity?
"""
class Solution(object):
    def verifyPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: bool
        """
        if preorder is None or preorder == []:
            return True
        lb = -2 ** 31
        stack = []
        for i in preorder:
            if i < lb:
                return False
            while stack and i > stack[-1]:
                lb = stack.pop()
            stack.append(i)
        return True

from binarySearchTree import *
a = Solution()
t = BST([10,5,12,2,6])
print(t.toList(order=-1))
print(a.verifyPreorder(t.toList(order=-1)) == True)
