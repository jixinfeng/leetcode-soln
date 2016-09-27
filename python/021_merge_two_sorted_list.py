"""
Merge two sorted linked lists and return it as a new list. The new list should
be made by splicing together the nodes of the first two lists.
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None and l2 is None:
            return None
        elif l1 is None:
            return l2
        elif l2 is None:
            return l1
        headSort=curSort=ListNode(None)
        while l1 is not None and l2 is not None:
            if l1.val<l2.val:
                curSort.val=l1.val
                l1=l1.next
            else:
                curSort.val=l2.val
                l2=l2.next
            curSort.next=ListNode(None)
            curSort=curSort.next
        if l1 is None:
            while l2 is not None:
                curSort.val=l2.val
                l2=l2.next
                curSort.next=ListNode(None)
                curSort=curSort.next
        elif l2 is None:
            while l1 is not None:
                curSort.val=l1.val
                l1=l1.next
                curSort.next=ListNode(None)
                curSort=curSort.next
        return headSort
