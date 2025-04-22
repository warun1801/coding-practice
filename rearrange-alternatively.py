from os import *
from sys import *
from collections import *
from math import *

def rearrange(arr):

    # Write your code here.
    pos = 0
    neg = 0
    
    # Find the first pos and neg number indices
    while pos < len(arr) and arr[pos] < 0:
        pos += 1

    while neg < len(arr) and arr[neg] >= 0:
        neg += 1        

    cur = 0
    while pos < len(arr) and neg < len(arr):
        # Swap the curr with pos at even indices and neg at odd indices
        if cur % 2 == 0:
            arr[cur], arr[pos] = arr[pos], arr[cur]
            pos += 1

        else:
            arr[cur], arr[neg] = arr[neg], arr[cur]
            neg += 1
        
        cur += 1

        # find the next pos and neg indices
        while pos < len(arr) and arr[pos] < 0:
            pos += 1

        while neg < len(arr) and arr[neg] >= 0:
            neg += 1        
 
    