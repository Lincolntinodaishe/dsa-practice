class Solution:
    def findLHS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        d = {}
        res = 0
        for i in nums:
            d[i] = d.get(i, 0)+1
        for i in d:
            if i+1 in d:
                curr_len = d[i+1] + d[i]
                res = max(res, curr_len)
        return res
        # count all numbers and check if +1 of the number exists if it exists count the len
        # do that for every number
        