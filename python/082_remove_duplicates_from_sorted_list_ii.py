"""
Given a sorted linked list, delete all nodes that have duplicate numbers,
leaving only distinct numbers from the original list.

For example,
Given 1->2->3->3->4->4->5, return 1->2->5.
Given 1->1->1->2->3, return 2->3.
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        solnHead = ListNode(None)
        solnHead.next = head
        prev = solnHead
        curr = head
        while curr and curr.next:
            if curr.val == curr.next.val:
                currVal = curr.val
                while curr and curr.val == currVal:
                    curr = curr.next
                prev.next = curr
            else:
                curr = curr.next
                prev = prev.next
        return solnHead.next
