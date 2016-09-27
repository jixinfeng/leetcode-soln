"""
Given two sparse matrices A and B, return the result of AB.

You may assume that A's column number is equal to B's row number.

Example:

    A = [
      [ 1, 0, 0],
      [-1, 0, 3]
    ]

    B = [
      [ 7, 0, 0 ],
      [ 0, 0, 0 ],
      [ 0, 0, 1 ]
    ]


         |  1 0 0 |   | 7 0 0 |   |  7 0 0 |
    AB = | -1 0 3 | x | 0 0 0 | = | -7 0 3 |
                      | 0 0 1 |
"""
class Solution(object):
    def multiply(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        ra=len(A)
        rb=len(B)
        ca=len(A[0])
        cb=len(B[0])
        C=[[0 for i in range(cb)] for j in range(ra)]
        for i in range(ra):
            if not any(A[i]):
                continue
            for j in range(cb):
                for k in range(ca):
                    if A[i][k]!=0 and B[k][j]!=0:
                        C[i][j]+=A[i][k]*B[k][j]
        return C

A = [
  [ 1, 0, 0],
  [-1, 0, 3]
]

B = [
  [ 7, 0, 0 ],
  [ 0, 0, 0 ],
  [ 0, 0, 1 ]
]
a=Solution()
print(a.multiply(A,B))
