class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        total = sum(nums)
        prev = 0
        count = 0

        for i in nums[:len(nums)-1]: #we dont want to include the last right element 
            prev += i
            if prev >= total - prev:
                count +=1
        return count