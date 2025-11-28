from collections import defaultdict, deque

def detect_cycle_directed_graph_bfs(V, edges):
    graph = defaultdict(list)
    indeg = [0 for i in range(V)]
    for u, v in edges:
        graph[u].append(v)
        indeg[v] += 1

    vis = [False for _ in range(V)]

    q = deque([u for u in range(V) if indeg[u] == 0])

    while q:
        u = q.popleft()
        vis[u] = True
        for v in graph[u]:
            indeg[v] -=1

            if indeg[v] == 0:
                q.append(v)
        

    return len(set(vis)) > 1
