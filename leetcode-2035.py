"""
2053. Kth Distinct String in an Array
"""
from collections import Counter

class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        ctr = Counter(arr)
        d = [c for c in ctr.keys() if ctr[c] == 1]
        if (len(d) < k):
            return ""
        return d[k-1]