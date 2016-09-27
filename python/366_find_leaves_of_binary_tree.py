"""
Given a binary tree, collect a tree's nodes as if you were doing this: Collect
and remove all leaves, repeat until the tree is empty.

Example:

    Given binary tree 
    
              1
             / \
            2   3
           / \     
          4   5    
    
    Returns [4, 5, 3], [2], [1].

Explanation:

    1. Removing the leaves [4, 5, 3] would result in this tree:
    
              1
             / 
            2          
    2. Now removing the leaf [2] would result in this tree:
    
              1          
    3. Now removing the leaf [1] would result in the empty tree:
    
              []         
    Returns [4, 5, 3], [2], [1].

Credits:

    Special thanks to @elmirap for adding this problem and creating all test cases.
"""
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def findLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        self.soln = []
        if root is None:
            return self.soln
        while root.left or root.right:
            self.soln.append([])
            self.pruneTree(root)
        self.soln.append([root.val])
        return self.soln

    def pruneTree(self, root):
        if root.left:
            if root.left.left is None and root.left.right is None:
                self.soln[-1].append(root.left.val)
                root.left = None
            else:
                self.pruneTree(root.left)
        if root.right:
            if root.right and root.right.left is None and root.right.right is None:
                self.soln[-1].append(root.right.val)
                root.right = None
            else:
                self.pruneTree(root.right)

t = TreeNode(1)
t.left = TreeNode(2)
t.right = TreeNode(3)
t.left.left = TreeNode(4)
t.left.right = TreeNode(5)

a = Solution()
print(a.findLeaves(t))
