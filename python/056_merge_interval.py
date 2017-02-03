"""
Given a collection of intervals, merge all overlapping intervals.

For example,
Given [1,3],[2,6],[8,10],[15,18],
return [1,6],[8,10],[15,18].
"""
# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if intervals is None or intervals == []:
            return []
        if len(intervals) == 1:
            return intervals
        intervals = sorted(intervals, key = lambda x : x.start)
        soln = [intervals[0]]
        for interval in intervals[1:]:
            if soln[-1].end >= interval.start:
                soln[-1].end = max(soln[-1].end, interval.end)
            else:
                soln.append(interval)
        return soln
