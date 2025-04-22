
"""
https://leetcode.com/problems/sum-of-all-subset-xor-totals/description/?envType=daily-question&envId=2025-04-05
1863. Sum of All Subset XOR Totals
The XOR total of an array is defined as the bitwise XOR of all its elements, or 0 if the array is empty.

For example, the XOR total of the array [2,5,6] is 2 XOR 5 XOR 6 = 1.
Given an array nums, return the sum of all XOR totals for every subset of nums. 

Note: Subsets with the same elements should be counted multiple times.

An array a is a subset of an array b if a can be obtained from b by deleting some (possibly zero) elements of b.
"""

# Crazy question
class Solution:

    def recurse(self, i, curr, nums):
        if i == len(nums):
            return curr

        ans1 = self.recurse(i + 1, curr ^ nums[i], nums)
        ans2 = self.recurse(i + 1, curr, nums)

        return ans1 + ans2

    def subsetXORSum(self, nums: List[int]):
        # Using bit manipulation O(n)
        # res = 0
        # for i in nums:
        #     res |= i

        # return res << (len(nums) - 1)
        return self.recurse(0, 0, nums)