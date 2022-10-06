"""
Design a data structure that supports the following two operations:

    void addWord(word)
    bool search(word)

search(word) can search a literal word or a regular expression string containing
only letters a-z or .. A . means it can represent any one letter.

For example:

    addWord("bad")
    addWord("dad")
    addWord("mad")
    search("pad") -> false
    search("bad") -> true
    search(".ad") -> true
    search("b..") -> true

Note:
    You may assume that all words are consist of lowercase letters a-z.

You should be familiar with how a Trie works. If not, please work on this
problem: Implement Trie (Prefix Tree) first.
"""


class WordDictionary:
    class TrieNode:
        def __init__(self, ch, end):
            self.ch = ch
            self.end = end
            self.leaves = {}

    def __init__(self):
        self.root = self.TrieNode(ch=None, end=False)

    def addWord(self, word: str) -> None:
        if not word:
            return
        p = self.root
        for c in word:
            if c not in p.leaves.keys():
                p.leaves[c] = self.TrieNode(ch=c, end=False)
            p = p.leaves[c]

        p.end = True

    def search(self, word: str) -> bool:
        return self._search(word, self.root)

    def _search(self, word, root):
        if not word:
            return root.end

        curr_char = word[0]
        word_tail = word[1:]
        if curr_char == '.':
            for child in root.leaves.values():
                if self._search(word_tail, child):
                    return True
            return False

        else:
            return curr_char in root.leaves.keys() and self._search(word_tail, root.leaves[curr_char])


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)

a = WordDictionary()
a.addWord('bad')
a.addWord('dad')
a.addWord('mad')
print(a.search("pad"))
print(a.search("bad"))
print(a.search(".ad"))
print(a.search("b.."))
