"""
Given a binary search tree and a node in it, find the in-order successor of that
node in the BST.

Note: If the given node has no in-order successor in the tree, return null.
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def find(self, root, p):
        if root is None:
            return None
        if root == p:
            return root
        if p.val < root.val:
            return self.find(root.left, p)
        if p.val > root.val:
            return self.find(root.right, p)
    
    def findMin(self, root):
        while root.left is not None:
            root = root.left
        return root

    def inorderSuccessor(self, root, p):
        """
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode
        """
        curr = self.find(root, p)
        if curr is None:
            return None
        elif curr.right is not None:
            return self.findMin(curr.right)
        else:
            successor = None
            ancestor = root
            while ancestor != curr:
                if curr.val < ancestor.val:
                    successor = ancestor
                    ancestor = ancestor.left
                else:
                    ancestor = ancestor.right
        return successor

"""
Note:
    https://www.youtube.com/watch?v=5cPbNCrdotA
"""
