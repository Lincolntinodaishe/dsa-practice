class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #Kadane Algorithm
        curr = 0
        max_total = float('-inf') # set the max total to negative infinity so that any negative number we come across is bigger
        for i in nums:
            curr += i
            max_total = max(curr, max_total)
            if curr < 0: # if curr is less than zero make it zero because if come across a positive number we want it to be the new maximum, 
                curr = 0
        return max_total