'''
123. Best Time to Buy and Sell Stock III
You are given an array prices where prices[i] is the price of a given stock on the ith day.
Find the maximum profit you can achieve. You may complete at most two transactions.
Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

Example 1:

Input: prices = [3,3,5,0,0,3,1,4]
Output: 6
Explanation: Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4-1 = 3.
Example 2:

Input: prices = [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are engaging multiple transactions at the same time. You must sell before buying again.
Example 3:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
'''

class Solution:
    def recursive(self, prices, ind, buy, sales):
        if sales == 0:
            return 0
        if ind == len(prices):
            return 0
        
        p1, p2 = 0, 0
        if buy == 1:
            # Lets buy
            p1 = self.recursive(prices, ind + 1, 0, sales) - prices[ind]
            # Lets not buy
            p2 = self.recursive(prices, ind + 1, 1, sales)
        else:
            # Lets sell
            p1 = prices[ind] + self.recursive(prices, ind + 1, 1, sales - 1)
            # Lets not sell
            p2 = self.recursive(prices, ind + 1, 0, sales)
        
        return max(p1, p2)

    def memoized(self, prices, ind, buy, sales, dp):
        if sales == 0:
            return 0
        if ind == len(prices):
            return 0

        if dp[ind][buy][sales] != -1:
            return dp[ind][buy][sales]
        
        p1, p2 = 0, 0
        if buy == 1:
            # Lets buy
            p1 = self.memoized(prices, ind + 1, 0, sales, dp) - prices[ind]
            # Lets not buy
            p2 = self.memoized(prices, ind + 1, 1, sales, dp)
        else:
            # Lets sell
            p1 = prices[ind] + self.memoized(prices, ind + 1, 1, sales - 1, dp)
            # Lets not sell
            p2 = self.memoized(prices, ind + 1, 0, sales, dp)
        
        dp[ind][buy][sales] = max(p1, p2)
        return dp[ind][buy][sales]

    def maxProfit(self, prices: List[int]) -> int:
        dp = [[[-1, -1, -1], [-1, -1, -1]] for i in range(len(prices))]
        return self.memoized(prices, 0, 1, 2, dp)


from typing import List

def tabulated(prices):
    dp = [[[0, 0, 0], [0, 0, 0]] for i in range(len(prices) + 1)]
    for i in range(len(prices) - 1, -1, -1):
        for j in range(2):
            for k in range(1, 3):
                # We can buy
                if j == 1:
                    # Lets buy
                    p1 = dp[i + 1][0][k] - prices[i]
                    # Lets not buy
                    p2 = dp[i + 1][1][k]
                    dp[i][j][k] = max(p1, p2)
                # We can sell
                else:
                    # Lets sell
                    p1 = dp[i + 1][1][k - 1] + prices[i]
                    # Lets not sell
                    p2 = dp[i + 1][0][k]
                    dp[i][j][k] = max(p1, p2)
    return dp[0][1][2]

def maxProfit(prices: List[int]) -> int:
    # Write your code here.
    return tabulated(prices)
    
'''
	Time Complexity: O(N)
	Space Complexity: O(1)

	Where N is the number of days.
'''
from typing import List
from sys import maxsize

def maxProfit(prices: List[int]) -> int:

    firstBuy, firstSell = -maxsize, 0
    secondBuy, secondSell = -maxsize, 0

    # Loop to consider each day.
    for i in range(len(prices)):

        # Maximum profit after buying the stock for the first time.
        firstBuy = max(firstBuy, - prices[i])

        # Maximum profit after selling the stock for the first time.
        firstSell = max(firstSell, firstBuy + prices[i])

        # Maximum profit after buying the stock for the second time.
        secondBuy = max(secondBuy, firstSell - prices[i])

        # Maximum profit after selling the stock for the second time.
        secondSell = max(secondSell, secondBuy + prices[i])

    # Return the final profit.
    return secondSell