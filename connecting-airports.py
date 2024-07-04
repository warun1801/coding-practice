'''
You are given a list of airports and a list of one way flights from one airport to another
eg. airport = ["BOM", "NGP", "BLR", "DEL", "GUW"]
flights = [[BOM, DEL], [DEL, NGP], ....]

You are given a starting airport, eg. NGP and you want to find the min. number of new flights required
to connect the airport to every other

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Requires Kosaraju's algorithm -
For finding strongly connected components in a directed graph

1. Find a DFS and add them to a stack after the recursive step
(This will ensure that the element taking the most time in the dfs step is at the top)

2. Create a transpose graph (reversed edges)

3. Write another dfs on the transposed graph to get the "who" array which will store the representative (in an SCC group)

4. You can now compress the graph using this who array to replace the entire SCC by one rep node.
'''

N = 10e5
adjList = [[] for i in range(N)]
adjTranspose = [[] for i in range(N)]
vis = [False for i in range(N)]
vis2 = [False for i in range(N)]
mp = {}
stack = []
who = [i for i in range(N)]

def dfs(u):
    vis[u] = True
    for v in adjList[u]:
        if not vis[v]:
            dfs[v]
    stack.append(u)
    
def dfs2(u, parent):
    vis2[u] = True
    for v in adjTranspose[u]:
        if not vis2[v]:
            dfs2[v, parent]
            
    who[u] = parent
        

def solve(airports: List[str], flights: List[List[str]], starting_flight: str):
    for i in range(len(airports)):
        mp[airports[i]] = i
        
    for u, v in flights:
        adjList[mp[u]].append(mp[v])
        adjList[mp[v]].append(mp[u])
        
    for i in range(len(airports)):
        if not vis[i]:
            dfs(i)
    
    while len(stack) > 0:
        top = stack.pop()
        if not vis2[top]:
            dfs2(top, top)
            
    in_degree = [0 for i in airports]
    
    for u in range(len(airports)):
        for v in adjList[u]:
            if who[u] != who[v]:
                in_degree[who[v]] += 1
                
    ans = 0
    for u in range(len(airports)):
        if u == who[u] and in_degree[u] == 0 and u != who[mp[starting_flight]]:
            ans += 1
            
    return ans


            
    
            
    
        
        
        
    
    
            
     
    