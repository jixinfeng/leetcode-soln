"""
Write a program to find the node at which the intersection of two singly linked
lists begins.

For example, the following two linked lists:
    
    A:          a1 → a2
                       ↘
                         c1 → c2 → c3
                       ↗            
    B:     b1 → b2 → b3
    begin to intersect at node c1.

Notes:
    If the two linked lists have no intersection at all, return null.

    The linked lists must retain their original structure after the function
    returns.

    You may assume there are no cycles anywhere in the entire linked structure.
    
    Your code should preferably run in O(n) time and use only O(1) memory.

Credits:
    Special thanks to @stellari for adding this problem and creating all test
    cases.
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if headA is None or headB is None:
            return None

        p, q = headA, headB
        while p != q:
            if p is None:
                p = headB
            else:
                p = p.next

            if q is None:
                q = headA
            else:
                q = q.next

            # if no intersection, they will reach the end at same time
        return p
