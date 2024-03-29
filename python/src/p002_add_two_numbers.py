"""
You are given two linked lists representing two non-negative numbers. The digits
are stored in reverse order and each of their nodes contain a single digit. Add
the two numbers and return it as a linked list.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
"""
from singlyLinkedList import *


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        solnHead = ListNode(None)
        p = solnHead
        carry = 0
        while l1 or l2 or carry:
            p.next = ListNode(carry)
            if l1:
                p.next.val += l1.val
                l1 = l1.next
            if l2:
                p.next.val += l2.val
                l2 = l2.next
            carry, p.next.val = divmod(p.next.val, 10)
            p = p.next
        return solnHead.next
