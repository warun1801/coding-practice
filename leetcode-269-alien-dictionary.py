"""
There is a new alien language which uses the latin alphabet. However, the order among letters are unknown to you. You receive a list of non-empty words from the dictionary, where words are sorted lexicographically by the rules of this new language. Derive the order of letters in this language.

Example 1:
Input:
["wrt", "wrf", "er", "ett", "rftt"]
Output: "wertf"

Example 2:
Input:
["z", "x"]
Output: "zx"
"""

"""
Clearly you need topological sorting between each word precedence relations

Topoloical sorting can be achieved by DFS in a Post Order manner
Also check if the graph is a DAG or not
Use a Path checker to just check if any node repeats in the path to check for a cycle
Other than that do a DFS and post order addition to the stack
"""

from collections import defaultdict



def solve(dictionary):
    
    # Create the Graph for the dictionary
    # according to the lexicographical order of the words
    # create directed graph dependencies
    graph = {c: set() for w in dictionary for c in w}
    for i in range(len(dictionary) - 1):
       w1, w2 = dictionary[i], dictionary[i+1]
       minlen = min(len(w1), len(w2))
       # in case there are any inconsistencies
       if len(w1) > len(w2) and w1[:minlen] == w2[:minlen]:
           return ""
       for j in range(minlen):
           if w1[j] != w2[j]:
               graph[w1[j]].add(w2[j])
               break
                      
    result = []
    vis = defaultdict(lambda: False)
    path = set() # for checking if there is a cycle for the DAG
    
    def dfs_for_topo(u):
        if u in path:
            return True
        
        vis[u] = True
        path.add(u)
        
        for v in graph[u]:
            if not vis[v] and not v in path:
                if dfs_for_topo(v):
                    return True
        
        result.append(u)
        path.remove(u)
        return False
    
    x = graph.keys()
    
    for w in x:
        if not vis[w]:
            if dfs_for_topo(w):
                return ""
            
    return "".join(reversed(result))
            
if __name__ == "__main__":
    dictionary = ["wrt", "wrf", "er", "ett", "rftt"]
    print(solve(dictionary))
    
                  
    
        
