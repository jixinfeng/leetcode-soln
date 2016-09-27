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
class WordDictionary(object):
    class TrieNode(object):
        def __init__(self):
            self.leaves = {}
            self.nil = False

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.root = self.TrieNode()

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        loc = self.root
        for c in word:
            if c not in loc.leaves:
                loc.leaves[c] = self.TrieNode()
            loc = loc.leaves[c]
        loc.nil = True

    def searchTail(self, tail, loc):
        if tail == '':
            return loc.nil
        for i, c in enumerate(tail):
            if c == '.':
                if loc.leaves == {}:
                    return False
                else:
                    for leaf in loc.leaves:
                        if self.searchTail(tail[i + 1:], loc.leaves[leaf]):
                            return True
                    return False
            elif c in loc.leaves:
                loc = loc.leaves[c]
            else:
                return False
        return loc.nil

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could
        contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        return self.searchTail(word, self.root)

# Your WordDictionary object will be instantiated and called as such:
# wordDictionary = WordDictionary()
# wordDictionary.addWord("word")
# wordDictionary.search("pattern")

a = WordDictionary()
a.addWord('bad')
a.addWord('dad')
a.addWord('mad')
print(a.search("pad"))
print(a.search("bad"))
print(a.search(".ad"))
print(a.search("b.."))
