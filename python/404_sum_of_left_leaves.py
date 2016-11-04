"""
Find the sum of all left leaves in a given binary tree.

Example:

        3
       / \
      9  20
        /  \
       15   7

There are two left leaves in the binary tree, with values 9 and 15 respectively.
Return 24.
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.soln = 0
        if root is not None:
            self.sumLefts(root)
        return self.soln

    def sumLefts(self, root, left = False):
        if root.left is None and root.right is None:
            if left:
                self.soln += root.val
            return
        else:
            if root.left is not None:
                self.sumLefts(root.left, left=True)
            if root.right is not None:
                self.sumLefts(root.right)

