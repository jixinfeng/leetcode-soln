"""
There is a new alien language which uses the latin alphabet. However, the order among letters are unknown to you. You receive a list of non-empty words from the dictionary, where words are sorted lexicographically by the rules of this new language. Derive the order of letters in this language.

Example 1:
Given the following words in dictionary,

[
  "wrt",
  "wrf",
  "er",
  "ett",
  "rftt"
]
The correct order is: "wertf".

Example 2:
Given the following words in dictionary,

[
  "z",
  "x"
]
The correct order is: "zx".

Example 3:
Given the following words in dictionary,

[
  "z",
  "x",
  "z"
]
The order is invalid, so return "".

Note:
You may assume all letters are in lowercase.
You may assume that if a is a prefix of b, then a must appear before b in the given dictionary.
If the order is invalid, return an empty string.
There may be multiple valid order of letters, return any one of them is fine.
"""
class Solution(object):
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        if words is None or words == []:
            return ""
        chars = set().union(*map(set, words))
        outs = {c : set() for c in chars}
        indegrees = {c : 0 for c in chars}
        for i in range(len(words) - 1):
            before, after = words[i], words[i + 1]
            for j in range(min(len(before), len(after))):
                if before[j] != after[j]:
                    if after[j] not in outs[before[j]]:
                        indegrees[after[j]] += 1
                        outs[before[j]].add(after[j])
                    break
        print(outs)
        print(indegrees)
        print(set().union(*outs.values()))

        q = [k for k, v in indegrees.items() if v == 0]
        soln = []
        print(q)
        while q:
            print("out:", outs)
            print("indegrees:", indegrees)
            print(q, soln)
            curr_char = q.pop()
            print("take", curr_char)
            soln.append(curr_char)
            for next_char in outs[curr_char]:
                indegrees[next_char] -= 1
                if indegrees[next_char] == 0:
                    print("found", next_char)
                    q.append(next_char)

        if max(indegrees.values()) > 0:
            return ""
        else:
            return "".join(soln)

a = Solution()
#words = ["wrt","wrf","er","ett","rftt"]
#print(a.alienOrder(words))
#words = ["z","x","y","x"]
#print(a.alienOrder(words))
#words = ["z", "z"]
#print(a.alienOrder(words))
#words = ["wrt","wrtkj"]
#print(a.alienOrder(words))
words = ["za","zb","ca","cb"]
print(a.alienOrder(words))
