"""
Given preorder and inorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if inorder is None or inorder == []:
            return None
        rVal = preorder.pop(0)
        root = TreeNode(rVal)
        rIdx = inorder.index(rVal)
        root.left = self.buildTree(preorder, inorder[:rIdx])
        root.right = self.buildTree(preorder, inorder[rIdx + 1:])
        return root
