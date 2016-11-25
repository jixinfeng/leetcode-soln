"""
Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

For example:

Given binary tree [3,9,20,null,null,15,7],

        3
       / \
      9  20
        /  \
       15   7

return its zigzag level order traversal as:

    [
      [3],
      [20,9],
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
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        soln = []
        thisLevel = [root]
        reverse = False
        while thisLevel:
            nextLevel = []
            for node in thisLevel:
                if node.left:
                    nextLevel.append(node.left)
                if node.right:
                    nextLevel.append(node.right)
            if reverse:
                soln.append([node.val for node in thisLevel][::-1])
            else:
                soln.append([node.val for node in thisLevel])
            reverse = not reverse
            thisLevel = nextLevel
        return soln
