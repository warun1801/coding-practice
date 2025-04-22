from math import *
from collections import *
from sys import *
from os import *

'''
You are given an unsorted array/list 'ARR' of 'N' integers. Your task is to return the length of the longest consecutive sequence.

The consecutive sequence is in the form ['NUM', 'NUM' + 1, 'NUM' + 2, ..., 'NUM' + L] where 'NUM' is the starting integer of the sequence and 'L' + 1 is the length of the sequence.

Note:

If there are any duplicates in the given array we will count only one of them in the consecutive sequence.
For example-
For the given 'ARR' [9,5,4,9,10,10,6].

Output = 3
The longest consecutive sequence is [4,5,6].
Follow Up:
Can you solve this in O(N) time and O(N) space complexity?
'''

def lengthOfLongestConsecutiveSequence(arr, n):
    # Write your code here.
    mp = defaultdict(bool)

    if n == 1 or len(set(arr)) == 1:
        return 1

    for i in arr:
        mp[i] = True

    mx = 1
    for i in arr:
        if not mp[i - 1]:
            curr = 1
            while mp[i + curr]:
                curr += 1
                mx = max(mx, curr)

    return mx

        


        



