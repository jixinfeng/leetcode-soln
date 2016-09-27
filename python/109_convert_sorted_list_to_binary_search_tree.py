"""
Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        if head is None:
            return None
        if head.next is None:
            return TreeNode(head.val)
        slow, fast = head, head.next.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        rootHead = slow.next
        slow.next = None
        root = TreeNode(rootHead.val)
        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(rootHead.next)
        return root
