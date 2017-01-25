"""
Sort a linked list using insertion sort.
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        p = ListNode(head.val - 1)
        p.next = head
        prev = p
        curr = p.next
        while curr:
            if prev.val <= curr.val:
                curr = curr.next
                prev = prev.next
                continue
            prev.next = curr.next
            ins = p
            while curr.val >= ins.next.val:
                ins = ins.next
            curr.next = ins.next
            ins.next = curr
            curr = prev.next
        return p.next
