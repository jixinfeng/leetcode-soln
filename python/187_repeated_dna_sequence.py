"""
All DNA is composed of a series of nucleotides abbreviated as A, C, G, and T,
for example: "ACGAATTCCG". When studying DNA, it is sometimes useful to identify
repeated sequences within the DNA.

Write a function to find all the 10-letter-long sequences (substrings) that
occur more than once in a DNA molecule.

For example,

    Given s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT",

Return:
    ["AAAAACCCCC", "CCCCCAAAAA"].
"""
class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        seqLen = 10
        if s is None or len(s) < seqLen:
            return []
        seen = {}
        l = len(s)
        for i in range(l - seqLen + 1):
            seq = s[i:i + seqLen]
            seen[seq] = seen.get(seq, 0) + 1
        return [seq for seq, freq in seen.items() if freq > 1]

a = Solution()
print(a.findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT") ==
      ["AAAAACCCCC", "CCCCCAAAAA"])
