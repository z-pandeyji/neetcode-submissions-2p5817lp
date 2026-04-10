class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n == 0:
            return 0
        
        min_price = prices[0]
        max_profit = 0

        i = 1
        while i < n:
            price = prices[i]
            if price < min_price:
                min_price = price
            else:
                profit = price - min_price
                if profit > max_profit:
                    max_profit = profit
            i += 1
        return max_profit
        