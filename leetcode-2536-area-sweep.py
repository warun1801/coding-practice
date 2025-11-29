"""
2536. Increment Submatrices by One
You are given a positive integer n, indicating that we initially have an n x n 0-indexed integer matrix mat filled with zeroes.

You are also given a 2D integer array query. For each query[i] = [row1i, col1i, row2i, col2i], you should do the following operation:

Add 1 to every element in the submatrix with the top left corner (row1i, col1i) and the bottom right corner (row2i, col2i). That is, add 1 to mat[x][y] for all row1i <= x <= row2i and col1i <= y <= col2i.
Return the matrix mat after performing every query.

 

Example 1:


Input: n = 3, queries = [[1,1,2,2],[0,0,1,1]]
Output: [[1,1,0],[1,2,1],[0,1,1]]
Explanation: The diagram above shows the initial matrix, the matrix after the first query, and the matrix after the second query.
- In the first query, we add 1 to every element in the submatrix with the top left corner (1, 1) and bottom right corner (2, 2).
- In the second query, we add 1 to every element in the submatrix with the top left corner (0, 0) and bottom right corner (1, 1).
Example 2:


Input: n = 2, queries = [[0,0,1,1]]
Output: [[1,1],[1,1]]
Explanation: The diagram above shows the initial matrix and the matrix after the first query.
- In the first query we add 1 to every element in the matrix.
 

Constraints:

1 <= n <= 500
1 <= queries.length <= 104
0 <= row1i <= row2i < n
0 <= col1i <= col2i < n
"""

class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        """
        There is a new concept called as Area Sweep.

        Similar to what we do for range updates in 1d where
        lets say if we want to add k for range [i, j]
        then make a diff array of all zeros and you add +k to diff[i] and -k to diff[j + 1]

        then finally to a prefix sum of this and add to the original array. The + k takes care 
        of the range update and the -k offsets so that it doesnt fuck up

        Similarly for 2d array its called Area sweep
        Given a range of r1, c1 -> r2, c2

        +k -> r1, c1
        -k -> r1 , c2 + 1
        -k -> r2 + 1, c1
        +k -> r2 + 1, c2 + 1 (the offset of doing the negative twice)


        Then finally for the area sweep you do
        diff[i][j] += diff[i - 1][j] + diff[i][j - 1] - diff[i - 1][j - 1] (Removing double counting by inclusion-exclusion principle)

        """
        s = [[0] * n for _ in range(n)]

        for r1, c1, r2, c2 in queries:
            s[r1][c1] += 1
            if r2 < n - 1: s[r2 + 1][c1] -= 1
            if c2 < n - 1: s[r1][c2 + 1] -= 1
            if r2 < n - 1 and c2 < n - 1: s[r2 + 1][c2 + 1] += 1

        for i in range(n):
            for j in range(n):
                top = 0 if i == 0 else s[i - 1][j]
                left = 0 if j == 0 else s[i][j - 1]
                common = 0 if i == 0 or j == 0 else s[i - 1][j - 1]
                s[i][j] += top + left - common
                
        return s


