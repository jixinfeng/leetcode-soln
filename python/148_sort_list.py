"""
Sort a linked list in O(n log n) time using constant space complexity.
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        slow, fast = head, head
        while fast.next and fast.next.next:
        # while fast and fast.next:
        # will cause infinity recursion when LL has length 2
            slow, fast = slow.next, fast.next.next
        h1, h2 = head, slow.next
        slow.next = None
        h1 = self.sortList(h1)
        h2 = self.sortList(h2)
        head = self.mergeList(h1, h2)
        return head

    def mergeList(self, head1, head2):
        if head1 is None:
            return head2
        if head2 is None:
            return head1
        mergeHead = ListNode(None)
        h = mergeHead
        while head1 and head2:
            if head1.val <= head2.val:
                h.next = head1
                h = h.next
                head1 = head1.next
            else:
                h.next = head2
                h = h.next
                head2 = head2.next
        if head1 is None:
            h.next = head2
        if head2 is None:
            h.next = head1
        return mergeHead.next
