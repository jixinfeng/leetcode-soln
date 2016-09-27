"""
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],
        3
       / \
      9  20
        /  \
       15   7
return its level order traversal as:
    [
      [3],
      [9,20],
      [15,7]
    ]
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        self.ans = []
        if root is None:
            return self.ans
        def addLevel(root, depth):
            while len(self.ans) <= depth:
                self.ans.append([])
            self.ans[depth].append(root.val)
            if root.left:
                addLevel(root.left, depth + 1)
            if root.right:
                addLevel(root.right, depth + 1)
        addLevel(root, 0)
        return self.ans
