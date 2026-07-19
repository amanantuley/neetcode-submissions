class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minP = 0 
        maxP = 0

        for i in range(len(prices)):
            if prices[i] < prices[i+1]:
                minP = prices[i]
            else :
                minP = prices[i+1]

        for j in range(len(prices) - 1):
            if prices[j] > prices[i]:
                maxP = prices[j]
            else :
                maxP = prices[i]

        profit = maxP - minP
        return profit
            
