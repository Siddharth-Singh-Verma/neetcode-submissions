class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit,buy=0,prices[0]

        for i in prices:
            profit=max(profit,i-buy)
            buy = min(i,buy)

        return profit