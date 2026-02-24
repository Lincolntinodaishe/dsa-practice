class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        #Brute force O(n)
        for i, n in enumerate(nums):
            if target == n:   #if target is n
                return i
            elif n > target:   #if n> target
                return i
        return len(nums)       #otherwise

        