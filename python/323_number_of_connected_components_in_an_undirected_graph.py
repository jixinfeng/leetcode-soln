"""
Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge
is a pair of nodes), write a function to find the number of connected components
in an undirected graph.

Example 1:

     0          3
     |          |
     1 --- 2    4
    
    Given n = 5 and edges = [[0, 1], [1, 2], [3, 4]], return 2.

Example 2:

     0           4
     |           |
     1 --- 2 --- 3

    Given n = 5 and edges = [[0, 1], [1, 2], [2, 3], [3, 4]], return 1.

Note:
    You can assume that no duplicate edges will appear in edges. Since all edges
    are undirected, [0, 1] is the same as [1, 0] and thus will not appear
    together in edges.
"""
class Solution(object):
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        self.nodes = n
        self.idx = list(range(n))
        self.size = [1] * n
        self.parts = n
        for edge in edges:
            self.union(edge)
        return self.parts

    def root(self, node):
        while node != self.idx[node]:
            self.idx[node] = self.idx[self.idx[node]]
            node = self.idx[node]
        return node

    def union(self, edge):
        p, q = edge[0], edge[1]
        rootp, rootq = self.root(p), self.root(q)
        if rootp == rootq:
            return
        elif self.size[rootp] > self.size[rootq]:
            self.idx[rootq] = rootp
            self.size[rootq] += self.size[rootp]
        else:
            self.idx[rootp] = rootq
            self.size[rootp] += self.size[rootq]
        self.parts -= 1

    def find(self, p, q):
        return self.root(p) == self.root(q)

"""
Note:
    Weighted Quick Union with Path Compression
    [Sample Java Code](http://algs4.cs.princeton.edu/15uf/QuickUnionPathCompressionUF.java.html)
"""
