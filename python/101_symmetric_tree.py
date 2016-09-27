"""
Given a binary tree, check whether it is a mirror of itself (ie, symmetric
around its center).

For example, this binary tree is symmetric:
        1
       / \
      2   2
     / \ / \
    3  4 4  3
But the following is not:
        1
       / \
      2   2
       \   \
       3    3
Note:
    Bonus points if you could solve it both recursively and iteratively.
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isNodeSymmetric(self,p,q):
        if p is None and q is None:
            return True
        elif p is not None and q is not None and p.val==q.val:
            return self.isNodeSymmetric(p.left,q.right) and self.isNodeSymmetric(p.right,q.left)
        else:
            return False
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        else:
            return self.isNodeSymmetric(root.left,root.right)
