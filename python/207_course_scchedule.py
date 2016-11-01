"""
There are a total of n courses you have to take, labeled from 0 to n - 1.

Some courses may have prerequisites, for example to take course 0 you have to
first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, is it
possible for you to finish all courses?

For example:

    2, [[1,0]]
    There are a total of 2 courses to take. To take course 1 you should have finished course 0. So it is possible.
    
    2, [[1,0],[0,1]]
    There are a total of 2 courses to take. To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.

Note:
    The input prerequisites is a graph represented by a list of edges, not
    adjacency matrices. Read more about how a graph is represented.

Hints:
    This problem is equivalent to finding if a cycle exists in a directed graph.
    If a cycle exists, no topological ordering exists and therefore it will be
    impossible to take all courses.
    
    Topological Sort via DFS - A great video tutorial (21 minutes) on Coursera
    explaining the basic concepts of Topological Sort.
    
    Topological sort could also be done via BFS.
"""
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        inDegs = {i : 0 for i in range(numCourses)}
        outEdges = {i : [] for i in range(numCourses)}
        for edge in prerequisites:
            head, tail = edge[0], edge[1]
            inDegs[head] += 1
            outEdges[tail].append(head)

        zeroInDegs = [i for i in range(numCourses) if inDegs[i] == 0]
        sortCount = 0
        while len(zeroInDegs) > 0:
            tail = zeroInDegs.pop()
            for head in outEdges[tail]:
                inDegs[head] -= 1
                if inDegs[head] == 0:
                    zeroInDegs.append(head)
            sortCount += 1
        return sortCount == numCourses

a = Solution()
print(a.canFinish(2, [[1, 0]]) == True)
print(a.canFinish(2, [[1, 0], [0, 1]]) == False)
print(a.canFinish(3, [[0, 1], [0, 2], [1, 2]]) == True)
