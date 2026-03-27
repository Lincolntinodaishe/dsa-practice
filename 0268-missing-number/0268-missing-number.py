class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        '''
        d = set()
        for i in nums:
            d.add(i)
        for i in range(len(nums)+1):
            if i not in d: 
                return i
        '''
    
        # use Gauss formula sum of n numbers from 1
        n = len(nums)
        return n*(n+1) // 2 - sum(nums)
        
'''
        #binary
        #the indice of every number is equal to that number when in oder
        nums.sort()
        n = len(nums)
        l, r = 0, n-1
        while l<=r:
            mid = (l+r)//2
            if nums[mid] == mid:
                l = mid+1
            else:
                r = mid-1
        return l
'''
        

    