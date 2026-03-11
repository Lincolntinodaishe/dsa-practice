class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        nums.sort()
        l,r = 0, len(nums)-1
        while nums[l]<0 and nums[r]>0:
            if abs(nums[l]) == nums[r]:
                return nums[r]
            elif abs(nums[l] ) < nums[r]:
                r-=1
            else:
                l+=1
        return -1

        