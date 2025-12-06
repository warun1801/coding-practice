"""
3625. Count Number of Trapezoids II
Solved
Hard
Topics
premium lock icon
Companies
Hint
You are given a 2D integer array points where points[i] = [xi, yi] represents the coordinates of the ith point on the Cartesian plane.

Return the number of unique trapezoids that can be formed by choosing any four distinct points from points.

A trapezoid is a convex quadrilateral with at least one pair of parallel sides. Two lines are parallel if and only if they have the same slope.

 

Example 1:

Input: points = [[-3,2],[3,0],[2,3],[3,2],[2,-3]]

Output: 2

Explanation:



There are two distinct ways to pick four points that form a trapezoid:

The points [-3,2], [2,3], [3,2], [2,-3] form one trapezoid.
The points [2,3], [3,2], [3,0], [2,-3] form another trapezoid.
Example 2:

Input: points = [[0,0],[1,0],[0,1],[2,1]]

Output: 1

Explanation:



There is only one trapezoid which can be formed.

 

Constraints:

4 <= points.length <= 500
–1000 <= xi, yi <= 1000
All points are pairwise distinct.
"""

from collections import defaultdict
import math
from math import gcd

class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        d = defaultdict(lambda: defaultdict(int))
        mids = defaultdict(lambda: defaultdict(int))

        def add_line(p1, p2):
            x1, y1 = p1
            x2, y2 = p2
            A = y2 - y1
            B = x1 - x2
            # normalize slope
            g = gcd(A, B) or 1
            a = A // g
            b = B // g
            C = A * x1 + B * y1
            c = C // g
            if a < 0 or (a == 0 and b < 0):
                a, b, c = -a, -b, -c
            d[(a, b)][c] += 1

            mid = ((x1 + x2) / 2, (y1 + y2) / 2)
            mids[mid][(a, b)] += 1
        
        n = len(points)
        for i in range(n - 1):
            for j in range(i + 1, n):
                p1 = (points[i][0], points[i][1])
                p2 = (points[j][0], points[j][1])

                add_line(p1, p2)

        ans = 0
        # print(d)

        for slope in d.keys():
            s = sum(d[slope].values())
            for i in d[slope].keys():
                s -= d[slope][i]
                ans += (s * d[slope][i])

        for m in mids.keys():
            s = 0
            for i in mids[m].keys():
                ans -= s * mids[m][i]
                s += mids[m][i]

        return ans



# from collections import defaultdict
# import math
# from math import gcd

# class Solution:
#     def countTrapezoids(self, points: List[List[int]]) -> int:
#         d = defaultdict(lambda: defaultdict(int))

#         def add_line(p1, p2):
#             x1, y1 = p1
#             x2, y2 = p2
#             A = y2 - y1
#             B = x1 - x2
#             # normalize slope
#             g = gcd(A, B) or 1
#             a = A // g
#             b = B // g
#             C = A * x1 + B * y1
#             c = C // g
#             if a < 0 or (a == 0 and b < 0):
#                 a, b, c = -a, -b, -c
#             d[(a, b)][c] += 1
        
#         n = len(points)
#         for i in range(n - 1):
#             for j in range(i + 1, n):
#                 p1 = (points[i][0], points[i][1])
#                 p2 = (points[j][0], points[j][1])

#                 add_line(p1, p2)

#         ans = 0
#         # print(d)

#         for slope in d.keys():
#             s = sum(d[slope].values())
#             for i in d[slope].keys():
#                 s -= d[slope][i]
#                 ans += (s * d[slope][i])

#         mid = defaultdict(list)
#         for i in range(n):
#             xi, yi = points[i]
#             for j in range(i+1, n):
#                 xj, yj = points[j]
#                 mid[(xi + xj, yi + yj)].append((i, j))

#         parallelograms = 0
#         for pairs in mid.values():
#             m = len(pairs)
#             if m < 2:
#                 continue
#             total = m * (m - 1) // 2

#             # group diagonals by normalized direction (reuse gcd + canonical sign)
#             dir_cnt = defaultdict(int)
#             for a, b in pairs:
#                 dx = points[b][0] - points[a][0]
#                 dy = points[b][1] - points[a][1]
#                 g = gcd(dx, dy) or 1
#                 dxn, dyn = dx // g, dy // g
#                 if dxn < 0 or (dxn == 0 and dyn < 0):
#                     dxn, dyn = -dxn, -dyn
#                 dir_cnt[(dxn, dyn)] += 1

#             degenerate = 0
#             for cnt in dir_cnt.values():
#                 if cnt >= 2:
#                     degenerate += cnt * (cnt - 1) // 2

#             parallelograms += (total - degenerate)

#         return ans - parallelograms

"""
class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        n = len(points)
        inf = 10**9 + 7
        slope_to_intercept = defaultdict(list)
        mid_to_slope = defaultdict(list)
        ans = 0

        for i in range(n):
            x1, y1 = points[i]
            for j in range(i + 1, n):
                x2, y2 = points[j]
                dx = x1 - x2
                dy = y1 - y2

                if x2 == x1:
                    k = inf
                    b = x1
                else:
                    k = (y2 - y1) / (x2 - x1)
                    b = (y1 * dx - x1 * dy) / dx

                mid = (x1 + x2) * 10000 + (y1 + y2)
                slope_to_intercept[k].append(b)
                mid_to_slope[mid].append(k)

        for sti in slope_to_intercept.values():
            if len(sti) == 1:
                continue

            cnt = defaultdict(int)
            for b_val in sti:
                cnt[b_val] += 1

            total_sum = 0
            for count in cnt.values():
                ans += total_sum * count
                total_sum += count

        for mts in mid_to_slope.values():
            if len(mts) == 1:
                continue

            cnt = defaultdict(int)
            for k_val in mts:
                cnt[k_val] += 1

            total_sum = 0
            for count in cnt.values():
                ans -= total_sum * count
                total_sum += count

        return ans
"""