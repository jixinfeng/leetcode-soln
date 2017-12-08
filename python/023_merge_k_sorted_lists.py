"""
Merge k sorted linked lists and return it as one sorted list. Analyze and
describe its complexity.
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if lists is None or lists == []:
            return None
        mergeCache = []
        p = ListNode(None)
        q = p

        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(mergeCache, (lists[i].val, i))

        while mergeCache:
            val, head_i = heapq.heappop(mergeCache)
            q.next = lists[head_i]
            q = q.next
            lists[head_i] = lists[head_i].next
            if lists[head_i]:
                heapq.heappush(mergeCache, (lists[head_i].val, head_i))

        return p.next
