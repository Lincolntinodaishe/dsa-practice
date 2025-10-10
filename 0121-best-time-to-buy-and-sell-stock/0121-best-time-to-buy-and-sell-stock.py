class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #bRUTE
        # O(n2) time complexity looping twice in one array
        max_profit = 0
        # for i in range(len(prices)):
        #     for j in range(i+1, len(prices)):
        #         profit = prices[j]-prices[i]
        #         if profit > max_profit:
        #             max_profit = profit
        # return max_profit
        l = 0
        r = 1
        while r < len(prices):
            if prices[r] > prices[l]:
                profit = prices[r] - prices[l]
                max_profit = max(profit, max_profit)
            else: l = r
            r += 1
        return max_profit