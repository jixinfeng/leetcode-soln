"""
Reverse a singly linked list.

Hint:
    A linked list can be reversed either iteratively or recursively. Could you
    implement both?
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        before = ListNode(0)
        while head:
            after = head.next
            head.next = before.next
            before.next = head
            head = after
        return before.next

"""
Note: Recursive solution
class Solution(object):
    def reverseList(self, head):
        return self.doReverse(head, None)
    
    def doReverse(self, head, newHead):
        if head is None:
            return newHead
        next = head.next
        head.next = newHead
        return self.doReverse(next, head)
"""
