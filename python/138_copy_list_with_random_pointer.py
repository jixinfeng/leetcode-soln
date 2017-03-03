"""
A linked list is given such that each node contains an additional random pointer
which could point to any node in the list or null.

Return a deep copy of the list.
"""
# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if head is None:
            return head
        curr = head
        while curr:
            p = curr.next
            curr.next = RandomListNode(curr.label)
            curr.next.next = p
            curr = p
        curr = head
        while curr:
            if curr.random:
                curr.next.random = curr.random.next
            else:
                curr.next.random = None
            curr = curr.next.next
        newhead = RandomListNode(0)
        newhead.next = head.next
        curr = head
        while curr:
            p = curr.next.next
            if p:
                curr.next.next = p.next
            else:
                curr.next.next = None
            curr.next = p
            curr = p
        return newhead.next

"""
Solved with the help of hash dictionary
    def copyRandomList(self, head):
        if head is None:
            return head
        table = {}
        table[None] = None
        curr = head
        while curr:
            table[curr] = RandomListNode(curr.label)
            curr = curr.next
        newhead = table[head]
        curr = head
        while curr:
            table[curr].next = table[curr.next]
            table[curr].random = table[curr.random]
            curr = curr.next
        return newhead
"""
