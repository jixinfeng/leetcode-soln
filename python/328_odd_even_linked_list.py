"""
Given a singly linked list, group all odd nodes together followed by the even
nodes. Please note here we are talking about the node number and not the value
in the nodes.

You should try to do it in place. The program should run in O(1) space
complexity and O(nodes) time complexity.

Example:
    Given 1->2->3->4->5->NULL,
    return 1->3->5->2->4->NULL.

Note:
    The relative order inside both the even and odd groups should remain as it
    was in the input. 
    The first node is considered odd, the second node even and so on ...

Credits:
    Special thanks to @DjangoUnchained for adding this problem and creating
    all test cases.
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return head
        if head.next is None:
            return head
        p = ListNode(None)
        p.next = head
        q = p.next
        if p.next.next is not None:
            r = ListNode(None)
            r.next = p.next.next
            s = r.next
        else:
            return head
        while q.next is not None and s.next is not None:
            if q.next is s:
                q.next = s.next
                q = s.next
            elif s.next is q:
                s.next = q.next
                s = q.next
        q.next = r.next
        s.next = None
        return p.next
