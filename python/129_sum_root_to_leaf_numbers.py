"""
Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.

An example is the root-to-leaf path 1->2->3 which represents the number 123.

Find the total sum of all root-to-leaf numbers.

For example,

    1
   / \
  2   3

The root-to-leaf path 1->2 represents the number 12.
The root-to-leaf path 1->3 represents the number 13.

Return the sum = 12 + 13 = 25.
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        return self.leafSum(root, 0)

    def leafSum(self, root, prefix):
        prefix *= 10
        prefix += root.val
        if not root.left and not root.right:
            return prefix 
        else:
            soln = 0
            if root.left:
                soln += self.leafSum(root.left, prefix)
            if root.right:
                soln += self.leafSum(root.right, prefix)
            return soln

from binarySearchTree import *
a = Solution()
t = BST([2,1,3])
print(a.sumNumbers(t.root) == 44)
