class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dict1 = {}
        n = len(nums)
        for i in nums:
            dict1[i] = dict1.get(i, 0)+1
        for key, value in dict1.items():
            if dict1[key] > n/2:
                return key
            else :
                continue
        
        
        