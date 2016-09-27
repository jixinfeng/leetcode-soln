"""
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as a binary tree in
which the depth of the two subtrees of every node never differ by more than 1.
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        else:
            return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool

        Note:
            Balanced Binary Tree doesn't mean maxDepth-minDepth<=1

            For this problem, a height-balanced binary tree is defined as a
            binary tree in which the depth of the two subtrees of every node
            never differ by more than 1.

            They are different.
        """
        if root is None:
            return True
        elif abs(self.maxDepth(root.left) - self.maxDepth(root.right)) <= 1:
            return self.isBalanced(root.left) and self.isBalanced(root.right)
        else:
            return False
