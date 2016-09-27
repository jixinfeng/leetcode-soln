"""
Implement an iterator over a binary search tree (BST). Your iterator will be
initialized with the root node of a BST.

Calling next() will return the next smallest number in the BST.

Note: next() and hasNext() should run in average O(1) time and uses O(h) memory,
where h is the height of the tree.

Credits:
    Special thanks to @ts for adding this problem and creating all test cases.
"""
# Definition for a  binary tree node
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.init = True
        if root is None:
            self.root = None
            self.minimum = None
            self.maximum = None
        else:
            self.root = root
            self.minimum = root
            while self.minimum.left is not None:
                self.minimum= self.minimum.left
            self.maximum = root
            while self.maximum.right is not None:
                self.maximum= self.maximum.right

    def hasNext(self):
        """
        :rtype: bool
        """
        if self.root is None:
            return False
        if self.init:
            return True
        return self.current.val <= self.maximum.val

    def next(self):
        """
        :rtype: int
        """
        if self.init:
            self.current = self.minimum
            self.init = False
        if self.current.right is not None:
            self.successor = self.current.right
            while self.successor.left is not None:
                self.successor = self.successor.left
        else:
            self.ancestor = self.root
            self.successor = None
            while self.ancestor != self.current:
                if self.current.val < self.ancestor.val:
                    self.successor = self.ancestor
                    self.ancestor = self.ancestor.left
                else:
                    self.ancestor = self.ancestor.right
        output = self.current.val
        self.current = self.successor
        return output
        

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())

"""
Solution using stacks
class BSTIterator(object):
    def __init__(self, root):
        self.stack = []
        self.pushLeft(root)

    def hasNext(self):
        return len(self.stack) > 0

    def next(self):
        current = self.stack.pop()
        self.pushLeft(current.right)
        return(current.val)

    def pushLeft(self, node):
        while node:
            self.stack.append(node)
            node = node.left
"""

