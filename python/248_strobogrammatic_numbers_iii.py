"""
Given two strings low and high that represent two integers low and high where low <= high, return the number of strobogrammatic numbers in the range [low, high].

A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).



Example 1:

Input: low = "50", high = "100"
Output: 3
Example 2:

Input: low = "0", high = "0"
Output: 1


Constraints:

1 <= low.length, high.length <= 15
low and high consist of only digits.
low <= high
low and high do not contain any leading zeros except for zero itself.
"""


class Solution:
    def strobogrammaticInRange(self, low: str, high: str) -> int:
        candidates = []
        low_int = int(low)
        high_int = int(high)
        for length in range(len(low), len(high) + 1):
            candidates += list(map(int, self.findStrobogrammatic(length)))

        return len([str(c) for c in candidates if low_int <= c <= high_int])

    def findStrobogrammatic(self, n: int) -> List[str]:
        if n == 1:
            return ["0", "1", "8"]

        flip_dict = {'0': '0', '1': '1', '6': '9', '8': '8', '9': '6'}

        candidates = ['1', '6', '8', '9']
        for i in range(1, n // 2):
            new_candidates = []
            for c in candidates:
                for d in flip_dict.keys():
                    new_candidates.append(c + d)

            candidates = new_candidates

        new_candidates = []
        for left in candidates:
            right = "".join([flip_dict[ch] for ch in reversed(left)])
            if n % 2:
                for mid in ["0", "1", "8"]:
                    new_candidates.append(left + mid + right)
            else:
                new_candidates.append(left + right)

        return new_candidates
