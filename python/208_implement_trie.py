"""
Implement a trie with insert, search, and startsWith methods.

Note:
    You may assume that all inputs are consist of lowercase letters a-z.
"""
class TrieNode(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.leaves = {}
        self.nil = False

class Trie(object):

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        loc = self.root
        for c in word:
            if c not in loc.leaves:
                loc.leaves[c] = TrieNode()
            loc = loc.leaves[c]
        loc.nil = True

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        loc = self.root
        for c in word:
            if c in loc.leaves:
                loc = loc.leaves[c]
            else:
                return False
        return loc.nil

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie
        that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        loc = self.root
        for c in prefix:
            if c in loc.leaves:
                loc = loc.leaves[c]
            else:
                return False
        return True

# Your Trie object will be instantiated and called as such:
# trie = Trie()
# trie.insert("somestring")
# trie.search("key")

a = Trie()
a.insert('apple')
a.insert('bug')
a.insert('applepie')
a.insert('but')
print(a.search('apple'))
print(a.search('app'))
print(a.startsWith('app'))
