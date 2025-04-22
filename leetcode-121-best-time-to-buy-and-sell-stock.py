def maxProfit(self, prices: List[int]) -> int:
    bigAfter = [i for i in prices]

    ans = 0
    for i in range(len(prices) - 2, -1, -1):
        bigAfter[i] = max(bigAfter[i+1], prices[i])
        ans = max(ans, bigAfter[i] - prices[i])

    return ans