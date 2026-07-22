class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans=0
        n=len(prices)
        min_price=prices[0]
        for i in range (n):
            current_profit=prices[i]-min_price
            ans=max(current_profit,ans)
            min_price=min(min_price,prices[i])
        return ans
       

          

        