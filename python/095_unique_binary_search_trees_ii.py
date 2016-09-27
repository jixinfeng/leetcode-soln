"""
Given an integer n, generate all structurally unique BST's (binary search trees) that store values 1...n.

For example,
Given n = 3, your program should return all 5 unique BST's shown below.

       1         3     3      2      1
        \       /     /      / \      \
         3     2     1      1   3      2
        /     /       \                 \
       2     1         2                 3
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def generateNode(self, val, left, right):
        node = TreeNode(val)
        node.left = left
        node.right = right
        return node

    def generateTreeList(self, first, last):
        return [self.generateNode(root, left, right)
                for root in range(first, last + 1)
                for left in self.generateTreeList(first, root - 1)
                for right in self.generateTreeList(root + 1, last)]\
                or [None]

    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n == 0:
            return []
        return self.generateTreeList(1, n)

"""
Note:
    https://discuss.leetcode.com/topic/15886/should-be-6-liner/7
"""
