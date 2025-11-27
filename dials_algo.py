from collections import deque, defaultdict
from math import inf

def dials_algorithm(graph, s, K, target = None):
    n = len(graph.keys())
    d = [inf for _ in range(n)]
    vis = [False for _ in range(n)]
    prev = [-1 for _ in range(n)]


    buckets = [deque() for _ in range(K + 1)]
    buckets[0].append(s)

    max_dist = (n - 1) * K

    curr = 0

    while curr <= max_dist:
        idx = curr % (K + 1)

        while not buckets[idx]:
            curr += 1
            idx = curr % (K + 1)
        
        u = buckets[idx].popleft()
        if vis[u] or d[u] < curr:
            continue

        vis[u] = True

        for v, w in graph[u].items():
            if d[u] + w < d[v]:
                d[v] = d[u] + w
                prev[v] = u

                buckets[(d[u] + w) % (K + 1)].append(v)

    # Can optionally print the path using prev
    return d[target]
                

            

        
        

