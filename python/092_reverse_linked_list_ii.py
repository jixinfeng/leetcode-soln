"""
Reverse a linked list from position m to n. Do it in-place and in one-pass.

For example:
Given 1->2->3->4->5->NULL, m = 2 and n = 4,

return 1->4->3->2->5->NULL.

Note:
Given m, n satisfy the following condition:
1 ≤ m ≤ n ≤ length of list.
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if m == n:
            return head
        p = ListNode(0)
        p.next = head
        q = p
        for _ in range(m - 1):
            q = q.next
        prev = q.next
        curr = prev.next
        for _ in range(n - m):
            after = curr.next
            curr.next = prev
            prev = curr
            curr = after
        q.next.next = curr
        q.next = prev
        return p.next
