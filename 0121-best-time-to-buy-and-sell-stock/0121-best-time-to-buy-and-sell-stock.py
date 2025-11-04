class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #Brute 
        res = 0
        # for i in range(len(prices)):
        #     for j in range(i, len(prices)):
        #         profit = prices[j] - prices[i]
        #         res = max(profit, res)
        # return res
        n= len(prices)
        l = 0
        r = 1
        while r<n and l<r:
            if prices[r]> prices[l]:
               profit = prices[r] - prices[l]
               res = max(res, profit)
            else:
                l = r
            r+=1
        return res
        # optimal
             