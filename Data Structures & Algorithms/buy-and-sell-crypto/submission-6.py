class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        size = len(prices)
        max_to_the_right = [0] * size
        i = size - 2
        while i >= 0:
            max_to_the_right[i] = max(max_to_the_right[i + 1], prices[i + 1])
            i -= 1
        
        result = []
        for i, price in enumerate(prices):
            result.append(max_to_the_right[i] - price)
        return max(max(result), 0)