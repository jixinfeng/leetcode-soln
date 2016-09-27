"""
Given a list, rotate the list to the right by k places, where k is non-negative.

For example:
    Given 1->2->3->4->5->NULL and k = 2,
    return 4->5->1->2->3->NULL.
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head is None:
            return None
        if head.next is None:
            return head
        nodes = []
        p = ListNode(None)
        p.next = head
        q = p
        while q.next is not None:
            q = q.next
            nodes.append(q)
        k %= len(nodes)
        if k == 0:
            return head
        newHead = nodes[-k]
        nodes[-k - 1].next = None
        nodes[-1].next = head
        return newHead
