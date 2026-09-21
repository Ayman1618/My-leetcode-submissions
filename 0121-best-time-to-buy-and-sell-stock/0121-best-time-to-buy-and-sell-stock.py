class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        profit = 0

        for el in prices[1:]:
            if min_price > el:
                min_price = el
            
            profit = max(profit, el - min_price)
        
        return profit