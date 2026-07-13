class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        size = len(prices)

        max_right = [0] * size

        for i in range(size - 2, -1, -1):
            max_right[i] = max(max_right[i+1], prices[i+1])
        
        max_profit = 0

        for i in range(size):
            profit = max_right[i] - prices[i]
            max_profit = max(max_profit, profit)
        return max_profit