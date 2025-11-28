from collections import defaultdict

def dfs_detect_cycles(V, edges):
    graph = defaultdict(list)

    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    vis = [False for i in range(V)]

    def dfs(u, parent):
        vis[u] = True

        for v in graph[u]:
            if not vis[v]:
                if dfs(v, u):
                    return True
            elif v != parent:
                return True
    
        return False

    for u in range(V):
        if not vis[u]:
            if dfs(u, -1):
                return True
    return False


    