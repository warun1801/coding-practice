"""
1802. Maximum Value at a Given Index in a Bounded Array
You are given three positive integers: n, index, and maxSum. You want to construct an array nums (0-indexed) that satisfies the following conditions:

nums.length == n
nums[i] is a positive integer where 0 <= i < n.
abs(nums[i] - nums[i+1]) <= 1 where 0 <= i < n-1.
The sum of all the elements of nums does not exceed maxSum.
nums[index] is maximized.
Return nums[index] of the constructed array.

Note that abs(x) equals x if x >= 0, and -x otherwise.

 

Example 1:

Input: n = 4, index = 2,  maxSum = 6
Output: 2
Explanation: nums = [1,2,2,1] is one array that satisfies all the conditions.
There are no arrays that satisfy all the conditions and have nums[2] == 3, so 2 is the maximum nums[2].
Example 2:

Input: n = 6, index = 1,  maxSum = 10
Output: 3
 

Constraints:

1 <= n <= maxSum <= 109
0 <= index < n
"""
class Solution:
    def maxValue(self, n: int, idx: int, maxSum: int) -> int:
        def get_sum(num_elems, mx_val):
            s = 0
            if num_elems >= mx_val:
                s += mx_val * (mx_val + 1) // 2
                s += (num_elems - mx_val)

            else:
                diff = mx_val - num_elems
                s = (mx_val * (mx_val + 1) // 2) - (diff * (diff + 1) // 2)

            return s
        
        def viable(x):
            curr = x
            num_elems_left = idx - 1 + 1
            num_elems_right = n - idx
            l, r = 0, 0

            if idx != 0:    
                l = get_sum(num_elems_left, x - 1)
            r = get_sum(num_elems_right, x)
            s = l + r
            print(x, l, r)

            return s <= maxSum

        lo = 0
        hi = maxSum

        while lo < hi:
            mid = (lo + hi + 1) // 2
            if not viable(mid):
                hi = mid - 1
            else:
                lo = mid
        return lo
