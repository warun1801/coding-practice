'''
3362. Zero Array Transformation III
You are given an integer array nums of length n and a 2D array queries where queries[i] = [li, ri].

Each queries[i] represents the following action on nums:

Decrement the value at each index in the range [li, ri] in nums by at most 1.
The amount by which the value is decremented can be chosen independently for each index.
A Zero Array is an array with all its elements equal to 0.

Return the maximum number of elements that can be removed from queries, such that nums can still be converted to a zero array using the remaining queries. If it is not possible to convert nums to a zero array, return -1.

 

Example 1:

Input: nums = [2,0,2], queries = [[0,2],[0,2],[1,1]]

Output: 1

Explanation:

After removing queries[2], nums can still be converted to a zero array.

Using queries[0], decrement nums[0] and nums[2] by 1 and nums[1] by 0.
Using queries[1], decrement nums[0] and nums[2] by 1 and nums[1] by 0.
Example 2:

Input: nums = [1,1,1,1], queries = [[1,3],[0,2],[1,3],[1,2]]

Output: 2

Explanation:

We can remove queries[2] and queries[3].

Example 3:

Input: nums = [1,2,3,4], queries = [[0,3]]

Output: -1

Explanation:

nums cannot be converted to a zero array even after using all the queries.

 

Constraints:

1 <= nums.length <= 105
0 <= nums[i] <= 105
1 <= queries.length <= 105
queries[i].length == 2
0 <= li <= ri < nums.length
'''

from collections import defaultdict
import heapq

class Solution:
    def maxRemoval(self, nums: List[int], queries: List[List[int]]):
        queries.sort(key=lambda x: x[0])
        # we are sorting here to select the widest range queries using the heap later        

        heap = []
        diffArray = [0] * (len(nums) + 1)
        op = 0
        j = 0

        for i, num in enumerate(nums):
            
            # we are iterating on each number and we are adding the diff array to the op to account for the range query operations like the prefix sum thing for diff array
            op += diffArray[i]
            
            # adding in all the queries that start at this index in heap to emulate max heap
            while j < len(queries) and queries[j][0] == i:
                heapq.heappush(heap, -queries[j][1])
                j += 1
                
            
            # if the num of operations is less than curr number keep going in the heap and do the diff array subtractions accordingly as well
            while op < num and heap and -heap[0] >= i:
                r = -heapq.heappop(heap)
                op += 1
                diffArray[r + 1] -=1

            # if even after all the queries we havent hit the target, fuck it
            if op < num:
                return -1

        # operations remaining in the heap are to be returned as they are useless
        return len(heap)


        
        

            

