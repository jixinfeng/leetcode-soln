"""
Design and implement a TwoSum class. It should support the following operations:
add and find.

    add - Add the number to an internal data structure.

    find - Find if there exists any pair of numbers which sum is equal to the
    value.

For example,
    add(1); add(3); add(5);
    find(4) -> true
    find(7) -> false
"""


class TwoSum:

    def __init__(self):
        self.counts = {}

    def add(self, number: int) -> None:
        self.counts[number] = self.counts.get(number, 0) + 1

    def find(self, value: int) -> bool:
        for i in self.counts.keys():
            j = value - i
            if j in self.counts and (i != j or self.counts[i] > 1):
                return True

        return False

# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)
