"""
You have a number of envelopes with widths and heights given as a pair of
integers (w, h). One envelope can fit into another if and only if both the width
and height of one envelope is greater than the width and height of the other
envelope.

What is the maximum number of envelopes can you Russian doll? (put one inside
other)

Example:
    Given envelopes = [[5,4],[6,4],[6,7],[2,3]], the maximum number of envelopes
    you can Russian doll is 3 ([2,3] => [5,4] => [6,7]).
"""
class Solution(object):
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        if envelopes is None or envelopes == []:
            return 0
        envelopes.sort(key = lambda envelope : (envelope[0], -envelope[1]))
        tails = [envelopes[0][1]]
        for envelope in envelopes[1:]:
            h = envelope[1]
            if h < tails[0]:
                tails[0] = h
            elif h > tails[-1]:
                tails.append(h)
            else:
                low, high = 0, len(tails)
                while low <= high:
                    mid = (low + high) // 2
                    if tails[mid] >= h:
                        high = mid - 1
                    else:
                        low = mid + 1
                tails[low] = h
        return len(tails)

a = Solution()
print(a.maxEnvelopes([[5,4],[6,4],[6,7],[2,3]]) == 3)

"""
Note:

https://discuss.leetcode.com/topic/28738/java-python-binary-search-o-nlogn-time-with-explanation
"""
