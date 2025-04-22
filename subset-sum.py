from os import *
from sys import *
from collections import *
from math import *


'''
NOTES:
Recursive is easy, just see if the adding ith elem to curr sum and excluding it both cases and store the result of both's OR 
in a dp array to memoize

dp[i][j] = subset of sum of 0 to ith elems can make a value of j

Same principal in iterative approach

dp[i][j] =  dp[i - 1][j] // That is to exclude it and still get the sum j
                ||
            dp[i - 1][j - arr[i]] // that is to get the sum to j if curr elem is included
'''


def recursive(arr, curr_sum, i, k, dp):
    if curr_sum == k:
        return True

    if i >= len(arr) or curr_sum > k:
        return False

    if dp[i][curr_sum] != -1:
        return dp[i][curr_sum]

    dp[i][curr_sum] = recursive(arr, curr_sum + arr[i], i + 1, k, dp) or recursive(arr, curr_sum, i + 1, k, dp)
    return dp[i][curr_sum]

def iterative(arr, k):
    n = len(arr)
    dp = [[False for i in range(k + 1)] for j in range(n)]
    for i in range(1, k+1):
        dp[0][i] = i == arr[0]
    
    for j in range(0, n):
        dp[j][0] = True

    for i in range(1, n):
        for j in range(1, k + 1):
            dp[i][j] = dp[i - 1][j] or (False if j < arr[i] else dp[i-1][j - arr[i]])

    return dp[len(arr) - 1][k]

def subsetSumToK(n, k, arr):
    # Write your code here
    # Return a boolean variable 'True' or 'False' denoting the answer
    dp = [[-1 for i in range(k + 1)] for j in range(n)]
    return iterative(arr, k)
    

    
    

