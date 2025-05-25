'''
16. 3Sum Closest
Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.

Return the sum of the three integers.

You may assume that each input would have exactly one solution.

 

Example 1:

Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
Example 2:

Input: nums = [0,0,0], target = 1
Output: 0
Explanation: The sum that is closest to the target is 0. (0 + 0 + 0 = 0).
'''


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        closest_diff = float('inf')
        ans = -1
        for i in range(n):
            j = i + 1
            k = n - 1
            while j < k:
                sm = nums[i] + nums[j] + nums[k]
                if closest_diff > abs(target - sm):
                    closest_diff = abs(target - sm)
                    ans = sm
                if target == sm:
                    break
                elif target < sm:
                    k -= 1
                else:
                    j += 1


        return ans