'''
2338. Count the Number of Ideal Arrays
https://leetcode.com/problems/count-the-number-of-ideal-arrays/description/?envType=daily-question&envId=2025-04-22
You are given two integers n and maxValue, which are used to describe an ideal array.

A 0-indexed integer array arr of length n is considered ideal if the following conditions hold:

Every arr[i] is a value from 1 to maxValue, for 0 <= i < n.
Every arr[i] is divisible by arr[i - 1], for 0 < i < n.
Return the number of distinct ideal arrays of length n. Since the answer may be very large, return it modulo 109 + 7.

 

Example 1:

Input: n = 2, maxValue = 5
Output: 10
Explanation: The following are the possible ideal arrays:
- Arrays starting with the value 1 (5 arrays): [1,1], [1,2], [1,3], [1,4], [1,5]
- Arrays starting with the value 2 (2 arrays): [2,2], [2,4]
- Arrays starting with the value 3 (1 array): [3,3]
- Arrays starting with the value 4 (1 array): [4,4]
- Arrays starting with the value 5 (1 array): [5,5]
There are a total of 5 + 2 + 1 + 1 + 1 = 10 distinct ideal arrays.



Fermat's little theorem states that
a^(p-1) is congruent to 1 (mod p)

And definition of modular inverse is basically
ax is congruent to 1 (mod p) then x is the modular inverse of a (mod p)

Using these two we know that - 
modulo inverse of a factorial is 
n! ^ (p-2) mod p
Given p is not a factor in n!
'''


class Solution:
    def idealArrays(self, n: int, maxi: int) -> int:
        m = min(n, 14)
        dp = [[0] * (m + 1) for _ in range(maxi + 1)]
        mod = 10 ** 9 + 7
        for i in range(1, maxi + 1):
            dp[i][1] = 1
            j = 2
            while i * j <= maxi:
                for k in range(1, m):
                    dp[i * j][k + 1] += dp[i][k]
                j += 1
        fact = [1 for i in range(n)]
        for i in range(1, n):
            fact[i] = fact[i - 1] * i % mod
        invFact = [1 for i in range(n)]
        invFact[n - 1] = pow(fact[n-1], mod - 2, mod)
        for i in range(n - 1, 0, -1):
            invFact[i - 1] = invFact[i] * i % mod

        res = 0
        for i in range(1, maxi + 1):
            for k in range(1, m + 1):
                res = (res + dp[i][k] * (fact[n-1] % mod * invFact[k - 1] % mod * invFact[n - k] % mod) % mod) % mod
        return res





