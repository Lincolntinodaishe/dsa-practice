class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        res = float('inf')
        nums.sort()
        l = 0
        for r in range(len(nums)):
            if r-l+1 >k:
                l+=1
            if r-l+1 == k:
                diff = nums[r]- nums[l]
                res = min(diff, res)
        return res

            
        
        