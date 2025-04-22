from os import *
from sys import *
from collections import *
from math import *
import heapq
from sys import stdin,setrecursionlimit

class Solution:
    def __init__ (self, start, end):
        self.start = start
        self.end = end

    def __lt__(self, other):
        if (self.start == other.start):
            return self.end > other.end
        else:
            return self.start < other.start
        
def merge(x, y):
    if x.start <= y.start <= y.end <= x.end:
        return x
    elif x.start <= y.start <= x.end < y.end:
        return Solution(x.start, y.end)
    
def isMergable(x, y):
    if x.end < y.start:
        return False
    return True
        
def mergeIntervals(intervals):
    # Write your code here.
    heapq.heapify(intervals)
    
    newList = []
    
    while intervals:
        x = heapq.heappop(intervals)
        if not intervals:
            newList.append(x)
        else:
            y = heapq.heappop(intervals)
            if isMergable(x, y):
                x = merge(x, y)
                heapq.heappush(intervals, x)
            else:
                newList.append(x)
                heapq.heappush(intervals, y)
    return newList
    

n = int(input())
arr1 = list(map(int, stdin.readline().strip().split(" ")))
arr2 = list(map(int, stdin.readline().strip().split(" ")))
intervals = []
for i in range(n):
    a = Solution(arr1[i], arr2[i])
    intervals.append(a)

res = mergeIntervals(intervals)

for i in range(len(res)):
    print(res[i].start, res[i].end)
