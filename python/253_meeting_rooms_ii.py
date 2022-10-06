"""
Given an array of meeting time intervals intervals where intervals[i] = [starti, endi], return the minimum number of
conference rooms required.



Example 1:

Input: intervals = [[0,30],[5,10],[15,20]]
Output: 2
Example 2:

Input: intervals = [[7,10],[2,4]]
Output: 1


Constraints:

1 <= intervals.length <= 10^4
0 <= starti < endi <= 10^6
"""


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        min_room = 0
        start_times = sorted([i[0] for i in intervals])
        end_times = sorted([i[1] for i in intervals])
        j = 0
        for i, start_time in enumerate(start_times):
            while end_times[j] <= start_time and j < len(end_times):
                j += 1
            min_room = max(min_room, i + 1 - j)

        return min_room
