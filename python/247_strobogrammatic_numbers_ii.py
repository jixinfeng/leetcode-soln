"""
Given an integer n, return all the strobogrammatic numbers that are of length n. You may return the answer in any order.

A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).



Example 1:

Input: n = 2
Output: ["11","69","88","96"]
Example 2:

Input: n = 1
Output: ["0","1","8"]


Constraints:

1 <= n <= 14
"""


class Solution:
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
