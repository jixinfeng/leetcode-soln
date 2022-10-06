"""
Given an m x n binary grid grid where each 1 marks the home of one friend, return the minimal total travel distance.

The total travel distance is the sum of the distances between the houses of the friends and the meeting point.

The distance is calculated using Manhattan Distance, where distance(p1, p2) = |p2.x - p1.x| + |p2.y - p1.y|.



Example 1:


Input: grid = [[1,0,0,0,1],[0,0,0,0,0],[0,0,1,0,0]]
Output: 6
Explanation: Given three friends living at (0,0), (0,4), and (2,2).
The point (0,2) is an ideal meeting point, as the total travel distance of 2 + 2 + 2 = 6 is minimal.
So return 6.
Example 2:

Input: grid = [[1,1]]
Output: 1


Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 200
grid[i][j] is either 0 or 1.
There will be at least two friends in the grid.
"""


class Solution:
    def minTotalDistance(self, grid: List[List[int]]) -> int:
        x_axis = []
        y_axis = []
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if grid[y][x] == 1:
                    x_axis.append(x)
                    y_axis.append(y)

        shortest_dist = 0
        x_axis = sorted(x_axis)
        y_axis = sorted(y_axis)
        i, j = 0, len(x_axis) - 1
        while j > i:
            shortest_dist += x_axis[j] - x_axis[i] + y_axis[j] - y_axis[i]
            i, j = i + 1, j - 1

        return shortest_dist
