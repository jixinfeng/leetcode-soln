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


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        seq_length = 10
        if len(s) < seq_length:
            return []

        count = {}
        for i in range(len(s) - seq_length + 1):
            seq = s[i: i + 10]
            count[seq] = count.get(seq, 0) + 1

        return [k for k, v in count.items() if v > 1]

a = Solution()
print(a.findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT") ==
      ["AAAAACCCCC", "CCCCCAAAAA"])
