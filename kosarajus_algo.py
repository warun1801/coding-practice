from collections import defaultdict

def kosaraju(V, edges):
    """
    To detect Strongly Connected Components - SCC

    The idea is to do a sort of a topological sort (not exactly since cycles can be but a dfs with stack)
    The order is reversed
    The apply dfs on a transposed graph in the now reversed order of the topo sort.
    The components of one dfs run are all scc components
    """

    graph = defaultdict(list)
    graph_rev = defaultdict(list)

    for u, v in edges:
        graph[u].append(v)
        graph_rev[v].append(u)

    vis = [False for i in range(V)]
    stack = []

    def stack_dfs(u):
        vis[u] = True
        
        for v in graph[u]:
            if not vis[v]:
                stack_dfs(v)

        stack.append(u)

    for u in range(V):
        if not vis[u]:
           stack_dfs(u)

    comps = set()
    scc = []
    vis = [False for _ in range(V)]
    
    def get_scc_dfs(u):
        vis[u] = True
        comps.add(u)

        for v in graph_rev[u]:
            if not vis[v]:
                get_scc_dfs(v)
    
    for u in reversed(stack):
        if not vis[u]:
            get_scc_dfs(u)

        scc.append(comps)
        comps = set()

    return comps


