"""
Given a binary tree, find the maximum path sum.

For this problem, a path is defined as any sequence of nodes from some starting
node to any node in the tree along the parent-child connections. The path does
not need to go through the root.

For example:
    Given the below binary tree,
    
           1
          / \
         2   3

    Return 6.
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxSubPathSum(self, root):
        if root is None:
            return -(2 ** 64) // 2, 0
        else:
            leftNNSum, leftRNSum = self.maxSubPathSum(root.left)
            rightNNSum, rightRNSum = self.maxSubPathSum(root.right)
            NNSum = max(leftNNSum, rightNNSum, \
                        root.val + leftRNSum + rightRNSum)
            RNSum = max(leftRNSum + root.val, rightRNSum + root.val, 0)
        return NNSum, RNSum

    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return -(2 ** 64) // 2
        else:
            maxNNSum, _ = self.maxSubPathSum(root)
            return maxNNSum
