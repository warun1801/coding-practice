'''
790. Domino and Tromino Tiling
Solved
Medium
Topics
Companies
You have two types of tiles: a 2 x 1 domino shape and a tromino shape. You may rotate these shapes.


Given an integer n, return the number of ways to tile an 2 x n board. Since the answer may be very large, return it modulo 109 + 7.

In a tiling, every square must be covered by a tile. Two tilings are different if and only if there are two 4-directionally adjacent cells on the board such that exactly one of the tilings has both squares occupied by a tile.

 

Example 1:


Input: n = 3
Output: 5
Explanation: The five different ways are show above.
Example 2:

Input: n = 1
Output: 1
 

Constraints:

1 <= n <= 1000
'''



MOD = 10**9+7

class Solution:
    def numTilings(self, n: int) -> int:
        '''
        n = 1 ans = 1
        n = 2 ans = 2
        n = 3 ans = 5
        n = 4 ans = 11
        n = 5 ans = 24
        n = 6 ans = 53
        n = 7 ans = 117
        '''
        dp = [-1 for i in range(10000)]
        dp[1] = 1
        dp[2] = 2
        dp[3] = 5
        dp[4] = 11
    
        def recurse(n, dp):
            if dp[n] == -1:
                dp[n] = (recurse(n - 3, dp) % MOD + (2 * recurse(n - 1, dp)) % MOD) % MOD
            return dp[n]
        
        return recurse(n, dp)
        

