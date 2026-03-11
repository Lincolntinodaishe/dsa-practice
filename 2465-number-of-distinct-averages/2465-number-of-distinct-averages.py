class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        nums.sort()
        s = set()
        l, r = 0, len(nums)-1
        while l<r:
            avg = (nums[l] + nums[r]) / 2
            s.add(avg)
            l+=1
            r-=1
        return len(s)


        
        