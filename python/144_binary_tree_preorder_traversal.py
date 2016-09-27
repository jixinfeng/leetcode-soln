"""
Given a binary tree, return the preorder traversal of its nodes' values.

For example:
Given binary tree {1,#,2,3},

   1
    \
     2
    /
   3

return [1,2,3].
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        traversal = []
        if root is None:
            return traversal
        traversalLeft = self.preorderTraversal(root.left)
        traversalRight = self.preorderTraversal(root.right)
        traversal.append(root.val)
        traversal += traversalLeft
        traversal += traversalRight
        return traversal

"""
Note: non-recursive version
    def preorderTraversal(self, root):
        nodeStack = []
        traversal = []
        if root is None:
            return traversal
        nodeStack.append(root)
        while nodeStack != []:
            currNode = nodeStack.pop()
            traversal.append(currNode.val)
            if currNode.right is not None:
                nodeStack.append(currNode.right)
            if currNode.left is not None:
                nodeStack.append(currNode.left)
        return traversal

"""
