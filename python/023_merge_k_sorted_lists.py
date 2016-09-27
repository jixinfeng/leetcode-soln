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
        for key in range(len(lists)):
            if lists[key] is not None:
                heapq.heappush(mergeCache, (lists[key].val, key))
                lists[key] = lists[key].next

        while len(mergeCache) > 0:
            node = heapq.heappop(mergeCache)
            val, key = node[0], node[1]
            q.next = ListNode(val)
            q = q.next
            if lists[key] is not None:
                heapq.heappush(mergeCache, (lists[key].val, key))
                lists[key] = lists[key].next
        return p.next
