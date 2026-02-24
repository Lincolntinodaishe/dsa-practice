class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        '''
        #Brute force O(n)
        for i, n in enumerate(nums):
            if target == n:   #if target is n
                return i
            elif n > target:   #if n> target
                return i
        return len(nums)       #otherwise
        '''
        # Binary Search
        l = 0
        r = len(nums)-1

        while r>=l:
            mid = (r+l)//2
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                r =mid-1
            else:
                l = mid+1
        return l
        