"""
Given a 2D board and a list of words from the dictionary, find all words in the
board.

Each word must be constructed from letters of sequentially adjacent cell, where
"adjacent" cells are those horizontally or vertically neighboring. The same
letter cell may not be used more than once in a word.

For example,
Given words = ["oath","pea","eat","rain"] and board =

    [
      ['o','a','a','n'],
      ['e','t','a','e'],
      ['i','h','k','r'],
      ['i','f','l','v']
    ]

    Return ["eat","oath"].

Note:
    You may assume that all inputs are consist of lowercase letters a-z.
    
    You would need to optimize your backtracking to pass the larger test. Could
    you stop backtracking earlier?
    
    If the current candidate does not exist in all words' prefix, you could stop
    backtracking immediately. What kind of data structure could answer such
    query efficiently? Does a hash table work? Why or why not? How about a Trie?
    If you would like to learn how to implement a basic trie, please work on
    this problem: Implement Trie (Prefix Tree) first.
"""
class TrieNode(object):
    def __init__(self):
        self.leaves = {}
        self.nil = False

class Trie(object):
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        loc = self.root
        for c in word:
            if c not in loc.leaves:
                loc.leaves[c] = TrieNode()
            loc = loc.leaves[c]
        loc.nil = True

class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        trie = Trie()
        for word in words:
            trie.insert(word)
        soln = set()
        x = len(board)
        y = len(board[0])
        for i in range(x):
            for j in range(y):
                self.search(board, words, i, j, trie.root, [], soln)
        return list(soln)

    def search(self, board, words, i, j, loc, path, soln):
        if loc.nil:
            soln.add("".join(path))
            loc.nil = False
        if i < 0 or i >= len(board) or\
           j < 0 or j >= len(board[0]):
            return
        currEntry = board[i][j]
        loc = loc.leaves.get(currEntry)
        if not loc:
            return
        board[i][j] = '#'
        path.append(currEntry)
        self.search(board, words, i - 1, j, loc, path, soln)
        self.search(board, words, i + 1, j, loc, path, soln)
        self.search(board, words, i, j - 1, loc, path, soln)
        self.search(board, words, i, j + 1, loc, path, soln)
        path.pop()
        board[i][j] = currEntry
        return

a = Solution()
board = \
    [
      ['o','a','a','n'],
      ['e','t','a','e'],
      ['i','h','k','r'],
      ['i','f','l','v']
    ]
words = ["oath","pea","eat","rain"]
print(a.findWords(board, words))

board = \
        [
            ['a','b'],
            ['c','d']
        ]
words = ['ab','cb','ad','bd','ac','ca','da','bc','db','adcb','dabc','abb','acb']
print(a.findWords(board, words))
