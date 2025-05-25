'''
3547. Maximum Sum of Edge Values in a Graph
You are given an undirected connected graph of n nodes, numbered from 0 to n - 1. Each node is connected to at most 2 other nodes.

The graph consists of m edges, represented by a 2D array edges, where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi.

You have to assign a unique value from 1 to n to each node. The value of an edge will be the product of the values assigned to the two nodes it connects.

Your score is the sum of the values of all edges in the graph.

Return the maximum score you can achieve.

 

Example 1:


Input: n = 4, edges = [[0,1],[1,2],[2,3]]

Output: 23

Explanation:

The diagram above illustrates an optimal assignment of values to nodes. The sum of the values of the edges is: (1 * 3) + (3 * 4) + (4 * 2) = 23.

Example 2:


Input: n = 6, edges = [[0,3],[4,5],[2,0],[1,3],[2,4],[1,5]]

Output: 82

Explanation:

The diagram above illustrates an optimal assignment of values to nodes. The sum of the values of the edges is: (1 * 2) + (2 * 4) + (4 * 6) + (6 * 5) + (5 * 3) + (3 * 1) = 82.

 

Constraints:

1 <= n <= 5 * 104
m == edges.length
1 <= m <= n
edges[i].length == 2
0 <= ai, bi < n
ai != bi
There are no repeated edges.
The graph is connected.
Each node is connected to at most 2 other nodes.
'''

from collections import defaultdict, deque

class Solution:
    def maxScore(self, n: int, edges: List[List[int]]) -> int:
        num_conn = defaultdict(int)
        if n == 1:
            return 1
        if n == 2:
            return 2

        for a, b in edges:
            num_conn[a] += 1
            num_conn[b] += 1

        is_connected = True
        if 1 in set(num_conn.values()):
            is_connected = False

        if not is_connected:
            nodes = [-1 for i in range(n)]
            nodes[0] = 1
            nodes[-1] = 2

            if n & 1:
                mid = n // 2
                nodes[mid] = n
                curr = n - 1
                left = mid - 1
                right = mid + 1
                while left > 0:
                    nodes[right] = curr
                    curr -= 1
                    nodes[left] = curr
                    curr -= 1
                    left -= 1
                    right += 1
            
            else:
                mid_l = n // 2 - 1
                mid_r = n // 2 
                curr = n
                while mid_l > 0:
                    nodes[mid_r] = curr
                    curr -= 1
                    nodes[mid_l] = curr
                    curr -= 1
                    mid_r += 1
                    mid_l -= 1

            ans = 0

            for i in range(n - 1):
                ans += (nodes[i] * nodes[i+1])

            return ans

        d = deque([n])
        right = True

        for i in range(n - 1, 0, -1):
            if right:
                d.append(i)
                right = False
            else:
                d.appendleft(i)
                right = True

        
        ans = 2
        # print(d)
        for i in range(n - 1):
            ans += d[i] * d[i + 1]

        return ans
