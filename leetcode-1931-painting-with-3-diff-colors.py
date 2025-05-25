'''
1931. Painting a Grid With Three Different Colors
You are given two integers m and n. Consider an m x n grid where each cell is initially white. You can paint each cell red, green, or blue. All cells must be painted.

Return the number of ways to color the grid with no two adjacent cells having the same color. Since the answer can be very large, return it modulo 109 + 7.

 

Example 1:


Input: m = 1, n = 1
Output: 3
Explanation: The three possible colorings are shown in the image above.
Example 2:


Input: m = 1, n = 2
Output: 6
Explanation: The six possible colorings are shown in the image above.
Example 3:

Input: m = 5, n = 5
Output: 580986
 

Constraints:

1 <= m <= 5
1 <= n <= 1000
'''

class Solution:
    def colorTheGrid(self, m: int, n: int) -> int:
        MOD = 10 ** 9 + 7
        total = 3 ** m

        dp = [[0] * total for _ in range(n + 1)]
        rowValid = [[0] * total for _ in range(total)]
        valid = []
        pattern = [[] for _ in range(total)]


        # make all the valid columns
        # Store the number in valid list and the ternary pattern in pattern list to be able to traverse
        for i in range(total):
            val = i
            for _ in range(m):
                pattern[i].append(val % 3)
                val //= 3

            if not any(pattern[i][j] == pattern[i][j + 1] for j in range(m - 1)):
                valid.append(i)


        # Initial row of the dp will always have 1 for the valid since there is but 1 row till now
        for i in valid:
            dp[1][i] = 1

        # eliminate all the invalid row patterns by checking if adjacent value is equal in a row
        for i in valid:
            for j in valid:
                rowValid[i][j] = 1
                if any(pattern[i][k] == pattern[j][k] for k in range(m)):
                    rowValid[i][j] = 0

        # dp[i][j] -> number of way from row[0... col i] to make the pattern ending with j as the pattern 
        for col in range(2, n + 1):
            for i in valid:
                ans = 0
                for j in valid:
                    if rowValid[i][j]:
                        ans = (ans + dp[col - 1][j]) % MOD
                dp[col][i] = ans % MOD

        return sum(dp[n]) % MOD
        



