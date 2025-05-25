'''
815. Bus Routes
You are given an array routes representing bus routes where routes[i] is a bus route that the ith bus repeats forever.

For example, if routes[0] = [1, 5, 7], this means that the 0th bus travels in the sequence 1 -> 5 -> 7 -> 1 -> 5 -> 7 -> 1 -> ... forever.
You will start at the bus stop source (You are not on any bus initially), and you want to go to the bus stop target. You can travel between bus stops by buses only.

Return the least number of buses you must take to travel from source to target. Return -1 if it is not possible.

 

Example 1:

Input: routes = [[1,2,7],[3,6,7]], source = 1, target = 6
Output: 2
Explanation: The best strategy is take the first bus to the bus stop 7, then take the second bus to the bus stop 6.
Example 2:

Input: routes = [[7,12],[4,5,15],[6],[15,19],[9,12,13]], source = 15, target = 12
Output: -1
 

Constraints:

1 <= routes.length <= 500.
1 <= routes[i].length <= 105
All the values of routes[i] are unique.
sum(routes[i].length) <= 105
0 <= routes[i][j] < 106
0 <= source, target < 106
'''


from collections import defaultdict, deque

class Solution:
    def numBusesToDestination(self, routes: List[List[int]], src: int, des: int) -> int:
        n = len(routes)
        visited = defaultdict(bool)
        route_map = defaultdict(list)

        if src == des:
            return 0
        
        routes = [set(i) for i in routes]

        for i in range(n-1):
            for j in range(1, n):
                if len(routes[i].intersection(routes[j])) > 0:
                    route_map[i].append(j)
                    route_map[j].append(i)

        queue = deque([])

        for i, route in enumerate(routes):
            if src in route:
                queue.append((i, 1))

        while queue:
            route_no, depth = queue.popleft()
            if not visited[route_no]:
                route = routes[route_no]
                if des in route:
                    return depth
                visited[route_no] = True
                for route_neigh in route_map[route_no]:
                    if not visited[route_neigh]:
                        queue.append((route_neigh, depth + 1))
        
        return -1