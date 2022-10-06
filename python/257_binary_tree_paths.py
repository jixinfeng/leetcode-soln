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
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if not root:
            return []

        paths = []
        stack = [(root, [str(root.val)])]  # (node, path) tuple

        while stack:
            print(list(map(lambda x: (x[0].val, x[1]), stack)))
            node, curr_path = stack.pop()

            if not node.left and not node.right:
                paths.append('->'.join(curr_path))

            if node.left:
                stack.append((node.left, curr_path + [str(node.left.val)]))

            if node.right:
                stack.append((node.right, curr_path + [str(node.right.val)]))

        return paths


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
