class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        profit = 0
        i = 1
        while i < n:
            if prices[i] > prices[i - 1]:
                profit += prices[i] - prices[i - 1]
            i += 1
        return profit
        