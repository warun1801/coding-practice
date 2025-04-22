from os import *
from sys import *
from collections import *
from math import *

from sys import stdin, stdout, setrecursionlimit

'''
You are given an array/list ARR consisting of N integers. Your task is to find all the distinct triplets present in the array which adds up to a given number K.

An array is said to have a triplet {ARR[i], ARR[j], ARR[k]} with sum = 'K' if there exists three indices i, j and k such that i!=j, j!=k and i!=j and ARR[i] + ARR[j] + ARR[k] = 'K'.

Note:
1. You can return the list of values in any order. For example, if a valid triplet is {1, 2, -3}, then {2, -3, 1}, {-3, 2, 1} etc is also valid triplet. Also, the ordering of different triplets can be random i.e if there are more than one valid triplets, you can return them in any order.
2. The elements in the array need not be distinct.
3. If no such triplet is present in the array, then return an empty list, and the output printed for such a test case will be "-1".
'''

def findTriplets(arr, n, target):
    
    # Write your code here.
    arr.sort()
    ans = []
    for i in range(n):
        if i != 0 and arr[i] == arr[i - 1]:
            continue
        j = i + 1
        k = n - 1     

        while j < k:
            sm = arr[i] + arr[j] + arr[k]
            if sm == target:
                ans.append([arr[i], arr[j], arr[k]])
                j += 1
                k -= 1
                while j < k and arr[j] == arr[j - 1]:
                    j += 1
                while j < k and arr[k] == arr[k + 1]:
                    k -= 1
            elif target > sm:
                j += 1
            else:
                k -= 1 
    return ans               



# Taking input using fast I/0.
def takeInput():
    N = int(stdin.readline())
    arr = list(map(int, stdin.readline().strip().split(" ")))
    K = int(stdin.readline())
    return N, arr,K


tc = int(input())
while tc > 0:
    N, arr,K = takeInput()
    ans = findTriplets(arr, N,K)

    if len(ans) == 0:
        stdout.write("-1\n")

    else:
        for i in ans:
            i.sort()
            stdout.write(str(i[0]) + " " + str(i[1]) + " " + str(i[2]) + "\n")

    tc -= 1
