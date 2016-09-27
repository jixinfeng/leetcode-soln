"""
Given a non-negative number represented as a singly linked list of digits, plus
one to the number.

The digits are stored such that the most significant digit is at the head of the
list.

Example:
    Input:
        1->2->3

    Output:
        1->2->4
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def plusOne(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        lastNotNine = None
        p = head
        while p is not None:
            if p.val != 9:
                lastNotNine = p
            p = p.next
        if lastNotNine is not None:
            lastNotNine.val += 1
            while lastNotNine.next is not None:
                lastNotNine = lastNotNine.next
                lastNotNine.val = 0
            return head
        else:
            newHead = ListNode(1)
            newHead.next = head
            q = ListNode(None)
            q.next = head
            while q.next is not None:
                q = q.next
                q.val = 0
            return newHead

"""
Recursive solution

class Solution(object):
    def plusOne(self, head):
        if head is not None:
            if self.calc(head):
                newHead = ListNode(1)
                newHead.next = head
                return newHead
        return head

    def calc(self, head):
        if head.next is None:
            if head.val == 9:
                head.val = 0
                return True
            else:
                head.val += 1
                return False
        elif self.calc(head.next):
            if head.val == 9:
                head.val = 0
                return True
            else:
                head.val += 1
                return False
"""
