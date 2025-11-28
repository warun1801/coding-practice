from collections import defaultdict

def graph_compression(V, graph, comps):
    comp_map = defaultdict(lambda: -1)
    i = 0
    for comp in comps:
        for c in comp:
            comp_map[c] = i
        i += 1

    

    condensed = [set() for _ in range(len(comps))]

    for u in range(V):
        cu = comp_map[u]
        for v in graph[u]:
            cv = comp_map[v]
            if cu != cv:
                condensed[cu].add(cv)

    return [list(u) for u in condensed]


