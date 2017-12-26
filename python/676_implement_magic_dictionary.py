"""
Implement a magic directory with buildDict, and search methods.

For the method buildDict, you'll be given a list of non-repetitive words to
build a dictionary.

For the method search, you'll be given a word, and judge whether if you modify
exactly one character into another character in this word, the modified word is
in the dictionary you just built.

Example 1:

Input: buildDict(["hello", "leetcode"]), Output: Null

Input: search("hello"), Output: False
Input: search("hhllo"), Output: True
Input: search("hell"), Output: False
Input: search("leetcoded"), Output: False

Note:

You may assume that all the inputs are consist of lowercase letters a-z.

For contest purpose, the test data is rather small by now. You could think
about highly efficient algorithm after the contest.

Please remember to RESET your class variables declared in class
MagicDictionary, as static/class variables are persisted across multiple test
cases. Please see here for more details.
"""
class MagicDictionary(object):
    class TrieNode(object):
        def __init__(self, x):
            self.key = x
            self.children = {}
            self.nil = False

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = self.TrieNode(None)

    def add(self, word):
        if not word:
            return
        p = self.root
        for w in word:
            if w not in p.children:
                p.children[w] = self.TrieNode(w)
            p = p.children[w]
        p.nil = True

    def buildDict(self, dict):
        """
        Build a dictionary through a list of words
        :type dict: List[str]
        :rtype: void
        """
        for word in dict:
            self.add(word)

    def search(self, word):
        """
        Returns if there is any word in the trie that equals to the given word
        after modifying exactly one character
        :type word: str
        :rtype: bool
        """
        if not word:
            return False
        discrepancy = 1
        stack = [(child, word, discrepancy)
                 for child in self.root.children.values()]
        while stack:
            curr_node, curr_word, curr_disc = stack.pop()
            if len(curr_word) == 1:
                if curr_node.nil:
                    if curr_disc == 0 and curr_word == curr_node.key:
                        return curr_node.nil
                    elif curr_disc == 1 and curr_word != curr_node.key:
                        return curr_node.nil
            else:
                for key, child in curr_node.children.items():
                    if curr_word[0] == curr_node.key:
                        stack.append((child, curr_word[1:], curr_disc))
                    elif curr_disc> 0:
                        stack.append((child, curr_word[1:], curr_disc - 1))
        return False

a = MagicDictionary()
a.buildDict(["hello","leetcode"])
a.buildDict(["hello","leetcode"])
assert a.search("hello") == False
assert a.search("hhllo") == True
assert a.search("hell") == False
assert a.search("leetcoded") == False
