"""
3016. Minimum Number of Pushes to Type Word II

You are given a string word containing lowercase English letters.

Telephone keypads have keys mapped with distinct collections of lowercase English letters, which can be used to form words by pushing them. For example, the key 2 is mapped with ["a","b","c"], we need to push the key one time to type "a", two times to type "b", and three times to type "c" .

It is allowed to remap the keys numbered 2 to 9 to distinct collections of letters. The keys can be remapped to any amount of letters, but each letter must be mapped to exactly one key. You need to find the minimum number of times the keys will be pushed to type the string word.

Return the minimum number of pushes needed to type word after remapping the keys.

An example mapping of letters to keys on a telephone keypad is given below. Note that 1, *, #, and 0 do not map to any letters.
"""

import heapq
from collections import Counter

def assign(l):
    vals_left = {1: 8, 2: 8, 3: 8}
    d = {}
    
    while l:
        _, w = heapq.heappop(l)
        for i in [1, 2, 3, 4, 5]:
            if (vals_left[i] != 0):
                d[w] = i
                vals_left[i] -= 1
                break
    return d
    

def minimumPushes(word: str):
    c = Counter(word)
    print(c)
    
    l = []
    for k in c.keys():
        l.append((-c[k], k))
        
    print(l)
    heapq.heapify(l)
    d = assign(l)
    
    ans = 0
    for w in word:
        ans += d[w]
        
    print(ans)
    
    
    
if __name__ == "__main__":
    minimumPushes("aremgjnptohswfdkyuzvicqxb")