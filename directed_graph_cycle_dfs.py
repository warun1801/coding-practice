from collections import defaultdict

def detect_cycles_directed_dfs(V, edges):
    graph = defaultdict(list)

    for u, v in edges:
        graph[u].append(v)

    vis = [False for _ in range(V)]
    stack = set()

    def dfs(u):
        vis[u] = True
        stack.add(u)
        for v in graph[u]:
            if not vis[v]:
                if dfs(v):
                    return True
            elif v in stack:
                return True
            
        stack.remove(u)
        return False
    
    for u in range(V):
        if not vis[u]:
            if dfs(u):
                return True
        
    return False