"""
Given a linked list, remove the nth node from the end of list and return its
head.

For example,

    Given linked list: 1->2->3->4->5, and n = 2.

    After removing the second node from the end, the linked list becomes
    1->2->3->5.

Note:
    Given n will always be valid.
    Try to do this in one pass.
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        placeHolder=ListNode(0)
        placeHolder.next=head
        p=q=placeHolder
        for i in range(n):
            p=p.next
        while p.next:
            p,q=p.next,q.next
        q.next=q.next.next
        return placeHolder.next
