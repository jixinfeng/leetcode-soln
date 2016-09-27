"""
Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

For example:
Given binary tree [3,9,20,null,null,15,7],
        3
       / \
      9  20
        /  \
       15   7
return its bottom-up level order traversal as:
    [
      [15,7],
      [9,20],
      [3]
    ]
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        self.levels=collections.defaultdict(list)
        self.ans=[]
        if root is None:
            return self.ans
        def addLevel(root, depth):
            self.levels[depth].append(root.val)
            if root.left:
                addLevel(root.left,depth+1)
            if root.right:
                addLevel(root.right,depth+1)
        addLevel(root,0)
        for i in range(len(self.levels.keys())):
            self.ans.append(self.levels[i])
        return self.ans[::-1]
