"""
Reverse a singly linked list.

Hint:
    A linked list can be reversed either iteratively or recursively. Could you
    implement both?
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        while curr:
            temp_next = curr.next
            curr.next = prev
            prev = curr
            curr = temp_next

        return prev


from singlyLinkedList import *

a = Solution()
ll1 = singlyLinkedList([1, 2, 3, 4, 5])
ll1.head = a.reverseList(ll1.head)

ll2 = singlyLinkedList([5, 4, 3, 2, 1])
print(ll1.isEqualTo(ll2))

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
