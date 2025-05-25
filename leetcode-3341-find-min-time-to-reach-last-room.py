'''
3341. Find Minimum Time to Reach Last Room I
Solved
Medium
Topics
Companies
Hint
There is a dungeon with n x m rooms arranged as a grid.

You are given a 2D array moveTime of size n x m, where moveTime[i][j] represents the minimum time in seconds when you can start moving to that room. You start from the room (0, 0) at time t = 0 and can move to an adjacent room. Moving between adjacent rooms takes exactly one second.

Return the minimum time to reach the room (n - 1, m - 1).

Two rooms are adjacent if they share a common wall, either horizontally or vertically.

 

Example 1:

Input: moveTime = [[0,4],[4,4]]

Output: 6

Explanation:

The minimum time required is 6 seconds.

At time t == 4, move from room (0, 0) to room (1, 0) in one second.
At time t == 5, move from room (1, 0) to room (1, 1) in one second.
Example 2:

Input: moveTime = [[0,0,0],[0,0,0]]

Output: 3

Explanation:

The minimum time required is 3 seconds.

At time t == 0, move from room (0, 0) to room (1, 0) in one second.
At time t == 1, move from room (1, 0) to room (1, 1) in one second.
At time t == 2, move from room (1, 1) to room (1, 2) in one second.
Example 3:

Input: moveTime = [[0,1],[1,2]]

Output: 3

 

Constraints:

2 <= n == moveTime.length <= 50
2 <= m == moveTime[i].length <= 50
0 <= moveTime[i][j] <= 109
'''

import heapq
from collections import defaultdict

class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        visited = defaultdict(list)
        n = len(moveTime)
        m = len(moveTime[0])
        
        def get_adj(x, y):
            adjList = set()
            for i in [-1, 1]:
                if 0 <= x + i < n:
                    adjList.add((x + i, y))
            
            for i in [-1, 1]:
                if 0 <= y + i < m:
                    adjList.add((x, y + i))
            return adjList

        heap = []
        for i, j in get_adj(0, 0):
            if not visited[(i, j)]:
                heapq.heappush(heap, (0, -i, -j))

        bomb = float('inf')
        while heap:
            # print(heap)
            curr_t, x, y = heapq.heappop(heap)
            x = -x
            y = -y
            if visited[(x, y)]:
                continue
            next_t = max(curr_t, moveTime[x][y]) + 1
            if (x, y) == (n - 1, m - 1):
                bomb = min(next_t, bomb)
            visited[(x, y)] = True
            for i, j in get_adj(x, y):
                heapq.heappush(heap, (next_t, -i, -j))
        
        return bomb