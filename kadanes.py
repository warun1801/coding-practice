from os import *
from sys import *
from collections import *
from math import *

from sys import stdin,setrecursionlimit
setrecursionlimit(10**7)

def maxSubarraySum(arr, n) :
    maxtill = 0
    maxtilltill = -float('inf')
    for i in range(n):
        maxtill = max(0, maxtill + arr[i])
        maxtilltill = max(maxtill, maxtilltill)
    return maxtilltill

def maxSubArraySum(self,arr):
        ##Your code here
        ## when atleast 1 number has to be there
        maxtill = -float('inf')
        maxtilltill = -float('inf')
        
        for i in arr:
            maxtill = max(i, i + maxtill)
            maxtilltill = max(maxtill, maxtilltill)
            
        return maxtilltill
