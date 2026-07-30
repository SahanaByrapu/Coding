""" https://leetcode.com/problems/best-time-to-buy-and-sell-stock/ """

class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        maxprofit=0
        minprice=sys.maxsize
        for i in range(len(prices)): 

            if(prices[i] < minprice):
             minprice=prices[i]

            maxprofit=max(maxprofit, prices[i]-minprice)

        return maxprofit
        
            
