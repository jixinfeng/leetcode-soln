"""
Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

You may assume that the intervals were initially sorted according to their start times.

Example 1:
Given intervals [1,3],[6,9], insert and merge [2,5] in as [1,5],[6,9].

Example 2:
Given [1,2],[3,5],[6,7],[8,10],[12,16], insert and merge [4,9] in as [1,2],[3,10],[12,16].

This is because the new interval [4,9] overlaps with [3,5],[6,7],[8,10].
"""
# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        if intervals is None or intervals == []:
            return [newInterval]
        s = newInterval.start
        e = newInterval.end
        left = [interval for interval in intervals if interval.end < s]
        right = [interval for interval in intervals if interval.start > e]
        if len(left) + len(right) < len(intervals):
            s = min(s, intervals[len(left)].start)
            e = max(e, intervals[-1 - len(right)].end)
        return left + [Interval(s, e)] + right

intervals = [Interval(*item) for item in [[1, 3], [6, 9]]]
assert [[interval.start, interval.end] for interval in Solution().insert(intervals, Interval(2, 5))] == [[1, 5], [6, 9]]

intervals = [Interval(*item) for item in [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]]
assert [[interval.start, interval.end] for interval in Solution().insert(intervals, Interval(4, 9))] == [[1, 2], [3, 10], [12, 16]]
