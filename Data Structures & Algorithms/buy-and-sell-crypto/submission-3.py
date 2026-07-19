
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        max_profit = 0

        for i in prices:
            if i < min_price:
                min_price = i

        for j in range(min_price + 1):
            if j > max_price:
                max_price = j
            
        max_profit = max_price - min_price
        return max_profit