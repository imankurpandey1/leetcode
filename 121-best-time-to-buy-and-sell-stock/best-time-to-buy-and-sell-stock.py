class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans=0
        min_price=prices[0]
        for i in range(len(prices)):
            cur_prof=prices[i]-min_price
            ans=max(cur_prof,ans)
            min_price=min(min_price,prices[i])
        return ans