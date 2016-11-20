"""
Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
Example 1:

    2
   / \
  1   3

Binary tree [2,1,3], return true.
Example 2:

    1
   / \
  2   3

Binary tree [1,2,3], return false.
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        bits = 64
        MAXINT = (2 ** bits) // 2 - 1
        MININT = -(2 ** bits) // 2
        return self.isValidSubTree(root, MININT, MAXINT) 

    def isValidSubTree(self, root, low, high):
        if root is None:
            return True
        elif root.val <= low or root.val >= high:
            return False
        return self.isValidSubTree(root.left, low, root.val) and \
                self.isValidSubTree(root.right, root.val, high)

from binarySearchTree import *
a = Solution()
t = BST([2,1,3])
print(a.isValidBST(t.root) == True)
t.root.val = 10
print(a.isValidBST(t.root) == False)
