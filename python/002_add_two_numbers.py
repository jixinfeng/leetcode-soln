"""
You are given two linked lists representing two non-negative numbers. The digits
are stored in reverse order and each of their nodes contain a single digit. Add
the two numbers and return it as a linked list.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
"""
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
        placeHolder=ListNode(0)
        p=placeHolder
        carry=0
        while l1 is not None and l2 is not None:
            digit=(l1.val+l2.val+carry)%10
            p.next=ListNode(digit)
            carry=(l1.val+l2.val+carry)//10
            l1=l1.next
            l2=l2.next
            p=p.next
            
        if l1 is None:
            while l2 is not None:
                digit=(l2.val+carry)%10
                p.next=ListNode(digit)
                carry=(l2.val+carry)//10
                l2=l2.next
                p=p.next
        elif l2 is None:
            while l1 is not None:
                digit=(l1.val+carry)%10
                p.next=ListNode(digit)
                carry=(l1.val+carry)//10
                l1=l1.next
                p=p.next

        if carry > 0:
            p.next=ListNode(carry)

        return placeHolder.next
