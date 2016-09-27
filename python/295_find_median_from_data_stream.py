"""
Median is the middle value in an ordered integer list. If the size of the list
is even, there is no middle value. So the median is the mean of the two middle
value.

Examples: 

    [2,3,4] , the median is 3

    [2,3], the median is (2 + 3) / 2 = 2.5

Design a data structure that supports the following two operations:

    void addNum(int num) - Add a integer number from the data stream to the data structure.

    double findMedian() - Return the median of all elements so far.

For example:

    add(1)
    add(2)
    findMedian() -> 1.5
    add(3) 
    findMedian() -> 2

Credits:

    Special thanks to @Louis1992 for adding this problem and creating all test cases.
"""
class MedianFinder:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.low, self.high = [], []

    def addNum(self, num):
        """
        Adds a num into the data structure.
        :type num: int
        :rtype: void
        """
        heapq.heappush(self.low, -heapq.heappushpop(self.high, num))
        if len(self.high) < len(self.low):
            heapq.heappush(self.high, -heapq.heappop(self.low))

    def findMedian(self):
        """
        Returns the median of current data stream
        :rtype: float
        """
        if len(self.high) > len(self.low):
            return float(self.high[0])
        else:
            return (self.high[0] - self.low[0]) / 2.0

# Your MedianFinder object will be instantiated and called as such:
# mf = MedianFinder()
# mf.addNum(1)
# mf.findMedian()

import heapq
a = MedianFinder()
for i in [40, 12, 16]:
    a.addNum(i)
    print(a.findMedian())

b = MedianFinder()
for i in range(1, 11):
    b.addNum(i)
    print(b.findMedian())
