'''
Problem statement
For a given integer array/list 'ARR' of size 'N' containing all distinct values, find the total number of 'Inversions' that may exist.

An inversion is defined for a pair of integers in the array/list when the following two conditions are met.

A pair ('ARR[i]', 'ARR[j]') is said to be an inversion when:

1. 'ARR[i] > 'ARR[j]' 
2. 'i' < 'j'

Where 'i' and 'j' denote the indices ranging from [0, 'N').
'''

from os import *
from sys import *
from collections import *
from math import *


def merge_inversions(arr, l, m, r):
    left = arr[l: m+1]
    right = arr[m+1: r+1]
    nl = len(left)
    nr = len(right)
    
    i, j, k = 0, 0, l
    ans = 0
    while i < nl and j < nr:
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
            ans += (nl - i) # Just adding count of all to the right (including itself) as they are bigger than it anyways
        k += 1
    
    while i < nl:
        arr[k] = left[i]
        k += 1
        i += 1
    
    while j < nr:
        arr[k] = right[j]
        k += 1
        j += 1
        
    return ans

def count_inversions(arr, l, r):
    ans = 0
    if l < r:
        m = (l + r) // 2  
        ans += count_inversions(arr, l, m)
        ans += count_inversions(arr, m + 1, r)
        
        ans += merge_inversions(arr, l, m, r)
        
    return ans


def getInversions(arr, n) :
	# Write your code here.
    
	return 

# Taking inpit using fast I/O.
def takeInput() :
    n = int(input())
    arr = list(map(int, stdin.readline().strip().split(" ")))
    return arr, n

# Main.
arr, n = takeInput()
print(getInversions(arr, n))