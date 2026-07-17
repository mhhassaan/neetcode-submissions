class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        minBuy = prices[0]

        for n in prices:
            maxProfit = max(maxProfit, n - minBuy)
            minBuy = min(minBuy, n)
        return maxProfit