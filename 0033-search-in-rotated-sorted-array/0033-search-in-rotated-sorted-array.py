class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # brute force O(n)
        # for i in range(len(nums)):
        #     if nums[i] == target:
        #         return i
        # return -1

        l = 0
        r = len(nums)-1

        while l<=r:
            mid = (l+r)//2
            if nums[mid] == target:
                return mid
            #check the left sorted part to see if target is in
            if nums[l] <= nums[mid]: #means its sorted
                if target < nums[l] or target > nums[mid]: # if target is not in that portion
                    l = mid+1
                else:
                    r = mid-1
            #check the right sorted part
            else:
                if target > nums[r] or target < nums[mid]:# if target nit in that portion
                    r = mid- 1
                else:
                    l = mid+1
        return -1


        