from collections import defaultdict

def topo_sort(n, edges):
    """
    You need to distinguish between already visited in the current path to the ones you are backtracking to.
    Hence the distinction between the visited values of 0, 1 and 2
    1 -> visited while traversing
    2 -> visited while backtracking
    0 -> unvisited

    This helps detects cycles
    """
    g = defaultdict(list)

    vis = [0 for _ in range(n + 1)]
    stack = []
    cycle = False
    for u, v in edges:
        g[u].append(v)

    def dfs(u):
        nonlocal cycle
        vis[u] = 1

        for v in g[u]:
            if vis[v] == 0:
                dfs(v)
            elif vis[v] == 1:
                cycle = True
        
        vis[u] = 2
        stack.append(u)

    for i in range(1, n + 1):
        if vis[i] == 0:
            dfs(i)

    if cycle:
        return None
    return list(reversed(stack))

if __name__ == "__main__":
    n = 5
    edges = [(1, 2), (1, 3), (2, 4), (3, 4), (4, 5)]

    print(topo_sort(n, edges))


