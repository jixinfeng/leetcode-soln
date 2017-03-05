"""
Given a singly linked list L: L0→L1→…→Ln-1→Ln,
reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

You must do this in-place without altering the nodes' values.

For example,
Given {1,2,3,4}, reorder it to {1,4,2,3}.
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        middlehead = slow.next
        slow.next = None

        if middlehead and middlehead.next:
            pre = middlehead
            cur = middlehead.next
            nxt = middlehead.next.next
            pre.next = None
            while nxt:
                cur.next = pre
                pre = cur
                cur = nxt
                nxt = nxt.next
            cur.next = pre
            head2 = cur
        elif middlehead:
            head2 = middlehead

        p, q = head, head2
        tmp1 = head.next
        tmp2 = head2.next
        while tmp1 and tmp2:
            p.next = q
            q.next = tmp1
            p, q = tmp1, tmp2
            tmp1, tmp2 = tmp1.next, tmp2.next
        p.next = q
        if tmp1:
            q.next = tmp1

from singlyLinkedList import singlyLinkedList
a = singlyLinkedList([1,2,3,4,5,6])
a.printNodes()
soln = Solution()
soln.reorderList(a.head)
a.printNodes()
