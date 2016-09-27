"""
Given a binary tree, return all root-to-leaf paths.

For example, given the following binary tree:

       1
     /   \
    2     3
     \
      5

All root-to-leaf paths are:

    ["1->2->5", "1->3"]

Credits:
    Special thanks to @jianchao.li.fighter for adding this problem and creating all test cases.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {string[]}
    def binaryTreePaths(self, root):
        self.paths=[]
        if root is None:
            return self.paths
        def dfs(root, path):
            if root.left is None and root.right is None:
                self.paths.append(path)
            if root.left:
                dfs(root.left,path+'->'+str(root.left.val))
            if root.right:
                dfs(root.right,path+'->'+str(root.right.val))
        dfs(root,str(root.val))
        return self.paths

"""
Shorter DFS from leetcode
https://leetcode.com/discuss/52020/5-lines-recursive-python

def binaryTreePaths(self, root):
    if not root:
        return []
    return [str(root.val) + '->' + path
            for kid in (root.left, root.right) if kid
            for path in self.binaryTreePaths(kid)] or [str(root.val)]

BFS Solution

def binaryTreePaths(self, root):
    from collections import deque
    if root is None:
        return []
    queue = deque( [ [root, str(root.val)] ] )
    ans = []
    while queue:
        front, path = queue.popleft()
        if front.left is None and front.right is None:
            ans += path,
            continue
        if front.left:
            queue += [front.left, path + "->" + str(front.left.val)],
        if front.right:
            queue += [front.right, path + "->" + str(front.right.val)],
    return ans
"""
