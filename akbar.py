from collections import defaultdict, deque

def akbar(n, r, m, edges, soldiers):
    """
    n - no. of cities
    r - no. of bidirectional 1 length roads
    m - no. of soldiers
    edges - city1, city2
    soldiers - base city, strength(radius)
    """

    vis = [False for i in range(n)]
    soldiers = [(c - 1, s) for c, s in soldiers] 

    graph = defaultdict(lambda: set())
    for u, v in edges:
        graph[u - 1].add(v - 1)
        graph[v - 1].add(u - 1)

    for city, s in soldiers:
        q = deque([(city, 0)])

        # have to do a level BFS
        while q:
            c, dist = q.popleft()
            vis[c] = True

            if dist == s:
                continue

            for v in graph[c]:
                if vis[v]:
                    return "No"
                q.append((v, dist + 1))
    return "No" if False in vis else "Yes"


def main():
    for _ in range(int(input())):
        n, r, m = map(int, input().strip().split())
        edges = []
        soldiers = []
        for i in range(r):
            edges.append(tuple(map(int, input().strip().split())))
        for i in range(m):
            soldiers.append(tuple(map(int, input().strip().split())))
        
        print(akbar(n, r, m, edges, soldiers))

if __name__ == "__main__":
    main()


