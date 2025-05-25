'''
22. Generate Parentheses
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()"]
'''

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def recurse(curr_str, left, right):
            if left == n and right == n:
                res.append(curr_str)
                return

            if left < n:
                recurse(curr_str + '(', left + 1, right)
            if right < left:
                recurse(curr_str + ')', left, right + 1)

        recurse('', 0, 0)
        return res