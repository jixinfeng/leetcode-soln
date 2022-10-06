"""
Given the root of a binary tree, return the number of uni-value subtrees.

A uni-value subtree means all nodes of the subtree have the same value.

Example 1:

Input: root = [5,1,5,5,5,null,5]
Output: 4
Example 2:

Input: root = []
Output: 0
Example 3:

Input: root = [5,5,5,5,5,null,5]
Output: 6

Constraints:

The number of the node in the tree will be in the range [0, 1000].
-1000 <= Node.val <= 1000
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        self.count = 0
        self.is_uni_val(root)
        return self.count

    def is_uni_val(self, node: Optional[TreeNode]) -> bool:
        if not node.left and not node.right:
            self.count += 1
            return True

        is_uni_val = True

        if node.left:
            is_uni_val = self.is_uni_val(node.left) and node.left.val == node.val

        if node.right:
            is_uni_val = self.is_uni_val(node.right) and is_uni_val and node.right.val == node.val

        self.count += is_uni_val

        return is_uni_val
