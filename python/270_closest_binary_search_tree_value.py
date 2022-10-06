"""
Given a non-empty binary search tree and a target value, find the value in the
BST that is closest to the target.

Note:
    Given target value is a floating point.

    You are guaranteed to have only one unique value in the BST that is closest
    to the target.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        values = self.inorder(root)
        return min(values, key=lambda x: abs(x - target))

    def inorder(self, node):
        return self.inorder(node.left) + [node.val] + self.inorder(node.right) if node else []
