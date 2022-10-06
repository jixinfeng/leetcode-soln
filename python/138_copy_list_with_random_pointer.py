"""
A linked list is given such that each node contains an additional random pointer
which could point to any node in the list or null.

Return a deep copy of the list.
"""
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head

        lookup = {}
        lookup[None] = None

        curr = head
        while curr:
            lookup[curr] = Node(curr.val)
            curr = curr.next

        curr = head
        while curr:
            lookup[curr].next = lookup[curr.next]
            lookup[curr].random = lookup[curr.random]
            curr = curr.next

        return lookup[head]
