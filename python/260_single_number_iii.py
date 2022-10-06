"""
Given an array of numbers nums, in which exactly two elements appear only once
and all the other elements appear exactly twice. Find the two elements that
appear only once.

For example:

    Given nums = [1, 2, 1, 3, 2, 5], return [3, 5].

Note:

    The order of the result is not important. So in the above example, [5, 3] is
    also correct.

    Your algorithm should run in linear runtime complexity. Could you implement
    it using only constant space complexity?

Credits:

    Special thanks to @jianchao.li.fighter for adding this problem and creating
    all test cases.
"""


class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        candidates = set()
        for n in nums:
            if n in candidates:
                candidates.remove(n)
            else:
                candidates.add(n)

        return list(candidates)


"""
Bit operation solution
http://bookshadow.com/weblog/2015/08/17/leetcode-single-number-iii/

    def singleNumber(self, nums):
        xor = reduce(lambda x, y : x ^ y, nums)
        lowbit = xor & -xor
        a = b = 0
        for num in nums:
            if num & lowbit:
                a ^= num
            else:
                b ^= num
        return [a, b]

    def singleNumber(self, nums):
        xor = reduce(operator.xor, nums)
        ans = reduce(operator.xor, filter(lambda x : x & xor & -xor, nums))
        return [ans, ans ^ xor]
"""
