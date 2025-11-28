from collections import deque, defaultdict

def topo_sort_kahn(n, edges):
    g = defaultdict(list)
    indegrees = [0] * (n + 1)

    for u, v in edges:
        g[u].append(v)
        indegrees[v] += 1

    q = deque([i for i in range(1, n + 1) if indegrees[i] == 0])
    ans = []

    while q:
        u = q.popleft()
        ans.append(v)

        for v in g[u]:
            indegrees[v] -= 1
            if indegrees[v] == 0:
                q.append(v)

    if len(ans) != n:
        return None
    
    return ans
        