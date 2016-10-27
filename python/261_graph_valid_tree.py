"""
Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge
is a pair of nodes), write a function to check whether these edges make up a
valid tree.

For example:

    Given n = 5 and edges = [[0, 1], [0, 2], [0, 3], [1, 4]], return true.

    Given n = 5 and edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]], return
    false.

Hint:

    Given n = 5 and edges = [[0, 1], [1, 2], [3, 4]], what should your return?
    Is this case a valid tree?

    According to the definition of tree on Wikipedia: “a tree is an undirected
    graph in which any two vertices are connected by exactly one path. In other
    words, any connected graph without simple cycles is a tree.”

Note: 
    you can assume that no duplicate edges will appear in edges. Since all edges
    are undirected, [0, 1] is the same as [1, 0] and thus will not appear
    together in edges.
"""
class Solution(object):
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        self.idx = [i for i in range(n)]
        self.sizes = [1] * n
        self.parts = n
        for edge in edges:
            p, q = edge[0], edge[1]
            if self.root(p) == self.root(q):
                return False
            else:
                self.union(edge)
        return self.parts == 1

    def root(self, p):
        while p != self.idx[p]:
            self.idx[p] = self.idx[self.idx[p]]
            p = self.idx[p]
        return p
            
    def union(self, edge):
        p, q = edge[0], edge[1]
        rootp, rootq = self.root(p), self.root(q)
        if self.sizes[p] < self.sizes[q]:
            self.idx[rootp] = rootq
            self.sizes[rootq] += self.sizes[rootp]
        else:
            self.idx[rootq] = rootp
            self.sizes[rootp] += self.sizes[rootq]
        self.parts -= 1

a = Solution()
print(a.validTree(5, [[0, 1], [0, 2], [0, 3], [1, 4]]) == True)
print(a.validTree(5, [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]) == False)
print(a.validTree(5, [[0, 1], [1, 2], [3, 4]]) == False)
