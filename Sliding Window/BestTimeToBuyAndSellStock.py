'''
Title - 121. Best Time to Buy and Sell Stock
Link - https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/
'''

class Solution:

    def maxProfitDp(self, prices: List[int]) -> int:
        min_price = prices[0]
        max_profit = 0
        n = len(prices)
        for i in range(1,n):
            price = prices[i]
            max_profit = max(max_profit, price-min_price)
            min_price = min(min_price, price)
        return max_profit
    
    def maxProfit2p(self, prices: List[int]) -> int:
        l,r,n,max_profit = 0,1,len(prices),0
        while r<n:
            if prices[l]<prices[r]:
                profit = prices[r]-prices[l]
                max_profit = max(max_profit, profit)
            else:
                l=r
            r+=1
        return max_profit

    def maxProfit(self, prices: List[int]) -> int:
        return self.maxProfitDp(prices)