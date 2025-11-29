"""
2654. Minimum Number of Operations to Make All Array Elements Equal to 1
You are given a 0-indexed array nums consisting of positive integers. You can do the following operation on the array any number of times:

Select an index i such that 0 <= i < n - 1 and replace either of nums[i] or nums[i+1] with their gcd value.
Return the minimum number of operations to make all elements of nums equal to 1. If it is impossible, return -1.

The gcd of two integers is the greatest common divisor of the two integers.

 

Example 1:

Input: nums = [2,6,3,4]
Output: 4
Explanation: We can do the following operations:
- Choose index i = 2 and replace nums[2] with gcd(3,4) = 1. Now we have nums = [2,6,1,4].
- Choose index i = 1 and replace nums[1] with gcd(6,1) = 1. Now we have nums = [2,1,1,4].
- Choose index i = 0 and replace nums[0] with gcd(2,1) = 1. Now we have nums = [1,1,1,4].
- Choose index i = 2 and replace nums[3] with gcd(1,4) = 1. Now we have nums = [1,1,1,1].
Example 2:

Input: nums = [2,10,6,14]
Output: -1
Explanation: It can be shown that it is impossible to make all the elements equal to 1.
 

Constraints:

2 <= nums.length <= 50
1 <= nums[i] <= 106
"""
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        def gcd(a, b):
            if a < b:
                return gcd(b, a)
            return a if b == 0 else gcd(b, a % b)

        if 1 in nums:
            return len(nums) - nums.count(1)
    
        def gcd_min_subarray_one():
            prev = []
            best = float('inf')

            for n in nums:
                new = [(n, 1)]

                for g, l in prev:
                    new_g = gcd(g, n)

                    # Check if gcd repeats
                    if new_g == new[-1][0]:
                        new[-1] = (new_g, min(l + 1, new[-1][1]))

                    else:
                        new.append((new_g, l + 1))

                for g, length in new:
                    if g == 1:
                        best = min(best, length)

                prev = new

            return best if best != float('inf') else -1

        s = gcd_min_subarray_one()
        if s == -1:
            return s
        else:
            return s + len(nums) - 2


        

        