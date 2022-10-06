"""
Given two 1d vectors, implement an iterator to return their elements
alternately.

For example, given two 1d vectors:

    v1 = [1, 2]
    v2 = [3, 4, 5, 6]
    By calling next repeatedly until hasNext returns false, the order of
    elements returned by next should be: [1, 3, 2, 4, 5, 6].

Follow up: What if you are given k 1d vectors? How well can your code be
extended to such cases?

Clarification for the follow up question - Update (2015-09-18):
    The "Zigzag" order is not clearly defined and is ambiguous for k > 2
    cases. If "Zigzag" does not look right to you, replace "Zigzag" with
    "Cyclic". For example, given the following input:

        [1,2,3]
        [4,5,6,7]
        [8,9]
    
    It should return [1,4,8,2,5,9,3,6,7].
"""


class ZigzagIterator:
    def __init__(self, v1: List[int], v2: List[int]):
        self.values = [v1, v2]
        self.idx = [0, 0]
        self.row = 0 if v1 else 1

    def next(self) -> int:
        next_row = (self.row + 1) % 2
        value = self.values[self.row][self.idx[self.row]]
        self.idx[self.row] += 1
        if self.idx[next_row] < len(self.values[next_row]):
            self.row = next_row

        return value

    def hasNext(self) -> bool:
        return self.idx[self.row] < len(self.values[self.row])

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())
