class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_profit = prices[0]
        n = 0
        for i in prices:
            if i < min_profit:
                min_profit = i
            max_profit = i - min_profit
            if n < max_profit:
                n = max_profit
        
        return n 