from collections import defaultdict, deque

LOG = 17 # for upto 10^5

def preprocess_lca(n, edges, root = 1):
    g = defaultdict(set)

    for u, v in edges:
        g[u].add(v)
        g[v].add(u)

    depth = [0 for _ in range(n + 1)]
    up = [[-1 for _ in range(n + 1)] for _ in range(LOG)]

    q = deque([root])
    up[0][root] = root # root is its own parent

    while q:
        u = q.popleft()
        for v in g[v]:
            # Check if its the parent or not
            if v == up[0][v]:
                continue
            up[0][v] = u
            depth[v] = depth[u] + 1

            q.append(v)

    # Binary lifting
    for k in range(1, LOG):
        for v in range(1, n + 1):
            up[k][v] = up[k - 1][up[k - 1][v]] # 2^k-1 th ancestor of 2^k-1 th ancestor of v

    return up, depth

def lca(u, v, up, depth):
    if depth[u] < depth[v]:
        v, u = u, v

    diff = depth[u] - depth[v]

    # Binary decomposition and trying to bring them to the same depth
    for k in range(LOG):
        if diff & (1 << k):
            u = up[k][u]

    if u == v:
        return v
    
    # We are bringing them up binary-ly biggest to smallest so as to not overshoot
    for k in reversed(range(LOG)):
        if up[k][u] != up[k][v]:
            u = up[k][u]
            v = up[k][v]

    return up[0][u]

