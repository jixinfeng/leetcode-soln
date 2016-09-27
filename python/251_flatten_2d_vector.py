"""
Implement an iterator to flatten a 2d vector.

For example,
    Given 2d vector =
    
    [
      [1,2],
      [3],
      [4,5,6]
    ]

By calling next repeatedly until hasNext returns false, the order of elements
returned by next should be: [1,2,3,4,5,6].

Hint:

    How many variables do you need to keep track?

    Two variables is all you need. Try with x and y.

    Beware of empty rows. It could be the first few rows.

    To write correct code, think about the invariant to maintain. What is it?

    The invariant is x and y must always point to a valid point in the 2d
    vector. Should you maintain your invariant ahead of time or right when you
    need it?

    Not sure? Think about how you would implement hasNext(). Which is more
    complex?

    Common logic in two different places should be refactored into a common
    method.
    
Follow up:
    As an added challenge, try to code it using only iterators in C++ or
    iterators in Java.
"""
class Vector2D(object):

    def __init__(self, vec2d):
        """
        Initialize your data structure here.
        :type vec2d: List[List[int]]
        """
        self.data = vec2d[::-1]
        while len(self.data) > 0:
            if type(self.data[-1]) is list:
                self.data += self.data.pop()[::-1]
            else:
                break

    def next(self):
        """
        :rtype: int
        """
        return self.data.pop()

    def hasNext(self):
        """
        :rtype: bool
        """
        while len(self.data) > 0:
            if type(self.data[-1]) is list:
                self.data += self.data.pop()[::-1]
            else:
                break
        return len(self.data) > 0
        

# Your Vector2D object will be instantiated and called as such:
# i, v = Vector2D(vec2d), []
# while i.hasNext(): v.append(i.next())
