"""
https://leetcode.com/problems/maximum-subarray-sum-with-length-divisible-by-k/description/?envType=daily-question&envId=2025-11-23

3381. Maximum Subarray Sum With Length Divisible by K
You are given an array of integers nums and an integer k.
Return the maximum sum of a subarray of nums, such that the size of the subarray is divisible by k.

Example 1:

Input: nums = [1,2], k = 1

Output: 3

Explanation:

The subarray [1, 2] with sum 3 has length equal to 2 which is divisible by 1.

Example 2:

Input: nums = [-1,-2,-3,-4,-5], k = 4

Output: -10

Explanation:

The maximum sum subarray is [-1, -2, -3, -4] which has length equal to 4 which is divisible by 4.

Example 3:

Input: nums = [-5,1,2,-3,4], k = 2

Output: 4

Explanation:

The maximum sum subarray is [1, 2, -3, 4] which has length equal to 4 which is divisible by 2.
Constraints:

1 <= k <= nums.length <= 2 * 10^5
-10^9 <= nums[i] <= 10^9


Idea is to maintain a list of all the k sums of all possible iterations (k max)
and then take kadanes of that :)
"""

from math import inf

class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        prefixSum = [nums[0]]

        for i in range(1, len(nums)):
            prefixSum.append(prefixSum[-1] + nums[i])

        def range_sum(i, j):
            if i == 0:
                return prefixSum[j]
            else:
                return prefixSum[j] - prefixSum[i - 1]

        def kadanes(arr):
            curr_max = -inf
            curr_max_max = -inf

            for i in range(len(arr)):
                curr_max = max(curr_max + arr[i], arr[i])
                curr_max_max = max(curr_max, curr_max_max)

            return curr_max_max

        n = len(nums)
        ans = -inf
        for offset in range(k):
            arr = []

            for j in range(offset, n, k):
                if j + k > n:
                    continue
                arr.append(range_sum(j, j + k - 1))

            # print(arr)
            # print(kadanes(arr))
            ans = max(ans, kadanes(arr))

        return ans