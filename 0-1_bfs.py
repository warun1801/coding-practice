from collections import deque, defaultdict
from math import inf

def bfs_0_1(V, edges, u, target):
    """
    Function returns the minimum distance from u to target if the edge weights
    are always either 0 or 1.

    Takes in V - no. of vertices
    edges - self explanatory (u, v, w -> edge weights)
    u - start node
    v - end node
    """

    def graph(V, edges):
        g = defaultdict(defaultdict(lambda: inf))
        for u, v, w in edges:
            g[u][v] = w
            g[v][u] = w

        return g

    q = deque([])
    d = [inf for _ in range(V)]
    d[u] = 0
    g = graph(V, edges)
    
    q.append(u)

    while q:
        u = q.popleft()

        for v, w in g[u].items():
            if (d[u] + w < d[v]):
                d[v] = d[u] + w
                if w == 0:
                    q.appendleft(v)
                else:
                    q.append(v)

    return d[target]
        
    
