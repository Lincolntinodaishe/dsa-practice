class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        res = float('inf')
        nums.sort()
        arr = []
        l = 0
        for r in range(len(nums)):
            arr.append(nums[r])
            if r-l+1 >k:
                arr.remove(nums[l])
                l+=1
            if r-l+1 == k:
                diff = arr[-1]- arr[0]
                res = min(diff, res)
        return res

            
        
        