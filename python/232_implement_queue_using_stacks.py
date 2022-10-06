"""
Implement the following operations of a queue using stacks.
    push(x) -- Push element x to the back of queue.
    pop() -- Removes the element from in front of queue.
    peek() -- Get the front element.
    empty() -- Return whether the queue is empty.

Notes:
    You must use only standard operations of a stack -- which means only push to
    top, peek/pop from top, size, and is empty operations are valid.
    Depending on your language, stack may not be supported natively. You may
    simulate a stack by using a list or deque (double-ended queue), as long as
    you use only standard operations of a stack.
    You may assume that all operations are valid (for example, no pop or peek
    operations will be called on an empty queue).
"""


class MyQueue:

    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    def push(self, x: int) -> None:
        while self.out_stack:
            self.in_stack.append(self.out_stack.pop())

        self.in_stack.append(x)

    def pop(self) -> int:
        while self.in_stack:
            self.out_stack.append(self.in_stack.pop())

        return self.out_stack.pop()

    def peek(self) -> int:
        while self.in_stack:
            self.out_stack.append(self.in_stack.pop())

        return self.out_stack[-1]

    def empty(self) -> bool:
        return len(self.in_stack) + len(self.out_stack) == 0

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
