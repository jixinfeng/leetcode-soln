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


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        in_degrees = [0] * numCourses
        out_edges = {node: [] for node in range(numCourses)}

        for course, prereq in prerequisites:
            in_degrees[course] += 1
            out_edges[prereq].append(course)

        zero_in_degs = [node for node, in_deg in enumerate(in_degrees) if in_deg == 0]
        count = 0
        while zero_in_degs:
            pre_req = zero_in_degs.pop()
            count += 1
            for course in out_edges[pre_req]:
                in_degrees[course] -= 1
                if in_degrees[course] == 0:
                    zero_in_degs.append(course)

        return count == numCourses


a = Solution()
print(a.canFinish(2, [[1, 0]]) is True)
print(a.canFinish(2, [[1, 0], [0, 1]]) is False)
print(a.canFinish(3, [[0, 1], [0, 2], [1, 2]]) is True)
