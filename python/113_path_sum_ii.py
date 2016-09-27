"""
Given a binary tree and a sum, find all root-to-leaf paths where each path's sum
equals the given sum.

For example:
    Given the below binary tree and sum = 22,

                  5
                 / \
                4   8
               /   / \
              11  13  4
             /  \    / \
            7    2  5   1

    return
    [
       [5,4,11,2],
       [5,8,4,5]
    ]
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, psum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        self.solns = []
        self.dfs(root, psum, [])
        return self.solns

    def dfs(self, root, psum, soln):
        if root.left is None and root.right is None:
            if psum == root.val:
                soln.append(root.val)
                self.solns.append(soln)
        if root.left:
            self.dfs(root.left, psum - root.val, soln + [root.val])
        if root.right:
            self.dfs(root.right, psum - root.val, soln + [root.val])
