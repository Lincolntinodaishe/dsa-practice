class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # #BRUTE 
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]
        # optimal
        #dict1 ={}
        #for i, n in enumerate(nums):
         #   diff = target - nums[i]
          #  if diff in dict1:
           #     return [dict1[diff], i]
            #dict1[nums[i]] = i

        d = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in d:
                return [d[diff], i]
            d[n] = i
                 
    
