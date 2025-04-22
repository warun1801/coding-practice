'''
Problem statement
You are given an array/list ‘ARR’ consisting of ‘N’ distinct integers arranged in ascending order. You are also given an integer ‘TARGET’. Your task is to count all the distinct pairs in ‘ARR’ such that their sum is equal to ‘TARGET’.

Note:

1. Pair (x,y) and Pair(y,x) are considered as the same pair. 

2. If there exists no such pair with sum equals to 'TARGET', then return -1.
Example:

Let ‘ARR’ = [1 2 3] and ‘TARGET’ = 4. Then, there exists only one pair in ‘ARR’ with a sum of 4 which is (1, 3). (1, 3) and (3, 1) are counted as only one pair.
'''
from os import *
from sys import *
from collections import *
from math import *

def pairSum(arr, n, target):
    # Write your code here.
    c = Counter(arr)
    visited = set()
    ans = 0
    for i in range(n):
        if not arr[i] in visited:
            visited.add(arr[i])
            visited.add(target - arr[i])

            if not arr[i] == (target - arr[i]):
                ans += (c[arr[i]] * c[target - arr[i]])

            else:
                ans += (c[arr[i]] * (c[arr[i]] - 1)) // 2

    return -1 if ans == 0 else ans