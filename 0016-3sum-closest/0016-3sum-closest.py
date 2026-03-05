class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest = float('inf')
        for i, a in enumerate(nums):
            if i > 0 and a == nums[i-1]:
                continue
            l = i+1
            r = len(nums)-1
            while l<r:
                curr = a + nums[l] + nums[r]
                if curr == target:
                    return curr
                if abs(target - curr) < abs(target - closest):
                    closest = curr
                if curr < target:
                    l+=1
                else:
                    r-=1         
        return closest
        #TIME = O(n^2)
        #Space O(n) - sorting