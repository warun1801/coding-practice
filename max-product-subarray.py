from os import *
from sys import *
from collections import *
from math import *

'''
Very easy question
Just parse the array from front and back once
Whenever you hit a zero start curr prod and set it to 1
and like kadanes try things out for max each loop
'''

def maximumProduct(arr, n):
    # write your code here
    # Return an integer denoting the answer to the required problem 
    mx = -float('inf')
    pre = 1
    suf = 1
    for i in range(0, n):
        if pre == 0:
            pre = 1
        if suf == 0:
            suf = 1
        pre *= arr[i]
        suf *= arr[n - 1 - i]

        mx = max(mx, pre, suf)
    return mx

