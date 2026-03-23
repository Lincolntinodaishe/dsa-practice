class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort() # sort numbers in order to do 2sum
        lst = []
        for i, a in enumerate(nums):
            if i>0 and a == nums[i-1]: # captur the first number then do 2sum to the rest avoiding repetition
                continue
            l = i+1
            r = len(nums)-1  #set pointers after the first char           
            while l<r:
                target = a + nums[l] + nums[r] # find the sum
                if target > 0:
                    r -=1
                elif target < 0:
                    l +=1
                else: 
                    lst.append([a, nums[l], nums[r]]) # add the correct value to the list
                    l += 1 # update l only since right wil updtae when tagrt is greater that 0
                    while l<r and nums[l] == nums[l-1] : # to avoid repetition in the pointer
                        l+=1
        return lst 


         

        
        
