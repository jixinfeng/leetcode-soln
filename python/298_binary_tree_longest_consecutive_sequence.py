"""
Given the root of a binary tree, return the length of the longest consecutive sequence path.

The path refers to any sequence of nodes from some starting node to any node in the tree along the parent-child
connections. The longest consecutive path needs to be from parent to child (cannot be the reverse).

Example 1:


Input: root = [1,null,3,2,4,null,null,null,5]
Output: 3
Explanation: Longest consecutive sequence path is 3-4-5, so return 3.
Example 2:


Input: root = [2,null,3,2,null,1]
Output: 2
Explanation: Longest consecutive sequence path is 2-3, not 3-2-1, so return 2.
 

Constraints:

The number of nodes in the tree is in the range [1, 3 * 104].
-3 * 104 <= Node.val <= 3 * 104
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        self.max_length: int = 0
        self.dfs(root, None, 0)
        return self.max_length

    def dfs(self, node: Optional[TreeNode], parent: Optional[TreeNode], length: int) -> int:
        if not node:
            return length

        if parent and node.val == parent.val + 1:
            length = length + 1
        else:
            length = 1

        self.max_length = max(self.max_length, length)

        self.dfs(node.left, node, length)
        self.dfs(node.right, node, length)
