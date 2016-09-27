"""
Given a stream of integers and a window size, calculate the moving average of
all integers in the sliding window.

For example,
MovingAverage m = new MovingAverage(3);
m.next(1) = 1
m.next(10) = (1 + 10) / 2
m.next(3) = (1 + 10 + 3) / 3
m.next(5) = (10 + 3 + 5) / 3
"""
class MovingAverage(object):

    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.size=size
        self.len=0
        self.data=[]

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        self.data.append(val)
        self.len+=1
        if self.len>self.size:
            del self.data[0]
            self.len-=1
        print(self.data)
        return 1.0*sum(self.data)/self.len

a=MovingAverage(1)
print(a.next(4))
print(a.next(0))
print(a.next(3))
print(a.next(5))

# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
