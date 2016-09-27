"""
Given a singly linked list, determine if it is a palindrome.

Follow up:
    Could you do it in O(n) time and O(1) space?
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None or head.next is None:
            return True
        placeHolder=ListNode(0)
        placeHolder.next=head
        p=placeHolder
        q=None
        while p.next:
            p=p.next
            r=ListNode(p.val)
            r.next=q
            q=r
        p=placeHolder.next
        while p.next:
            if p.val!=q.val:
                return False
            else:
                p=p.next
                q=q.next
        return True

"""
Faster and resourse friendlier solution from:
http://bookshadow.com/weblog/2015/07/10/leetcode-palindrome-linked-list/
    def isPalindrome(self, head):
        if head is None:
            return True
        #find mid node
        fast = slow = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        #reverse second half
        p, last = slow.next, None
        while p:
            next = p.next
            p.next = last
            last, p = p, next
        #check palindrome
        p1, p2 = last, head
        while p1 and p1.val == p2.val:
            p1, p2 = p1.next, p2.next
        #resume linked list(optional)
        p, last = last, None
        while p:
            next = p.next
            p.next = last
            last, p = p, next
        slow.next = last
        return p1 is None
"""
