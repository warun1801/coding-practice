def tarjan_low_link(graph):
    """
    tin[i] = time when reached the node (strictly increasing)
    low[i] = lowest possible reachable ancestor (timewise)
    low[i] = min(tin[i], tin[back edged ancestor], low[v] for v in childs])

    bridge (u-v): if low[v] > tin[u]
    articulation point (u): if low[v] >= tin[u]
    bcc: all (u-v) edges from the stack of the dfs where low[v] >= tin[u]
    """
    
    V = len(graph)

    tin = [-1] * V
    low = [-1] * V
    timer = 0

    bridges = []
    articulation = set()
    bccs = []
    edge_stack = []

    def dfs(u, parent):
        nonlocal timer
        tin[u] = low[u] = timer
        timer += 1

        childs = 0

        for v in graph[v]:
            if v == parent:
                continue
            
            if tin[v] == -1:
                # This is a Tree-edge condition

                edge_stack.append((u, v))

                dfs(v, u)
                low[u] = min(low[u], low[v])

                # Bridge condition
                if low[v] > tin[u]:
                    bridges.append((u, v))

                # Articulation point condition where node isnt the root
                if low[v] >= tin[u] and parent != -1:
                    articulation.add(u)

                # BCCs
                if low[v] >= tin[u]:
                    bcc = []
                    while edge_stack and edge_stack[-1] != (u, v):
                        bcc.append(edge_stack.pop())
                    bcc.append(edge_stack.pop())
                    bccs.append(bcc)

                childs += 1
            else:
                # already visited and so its a back-edge condition
                if tin[v] < tin[u]:
                    edge_stack.append((u, v))

                low[u] = min(low[u], tin[v])

        # Root articulation point condition
        if parent == -1 and childs > 1:
            articulation.add(u)


    for i in range(V):
        if tin[i] == -1:
            dfs(i, -1)

            # If not empty, pop remaining edges as single-edge BCCs or a final BCC:
            # Prefer to pop single-edge BCCs (each leftover edge is a bridge)
            while edge_stack:
                e = edge_stack.pop()
                bccs.append([e])

    return bridges, articulation, bccs                    

    