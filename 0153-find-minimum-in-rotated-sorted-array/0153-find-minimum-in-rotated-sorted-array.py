class Solution:
    def findMin(self, nums: List[int]) -> int:
        # o(n)
        # return min(nums)


        # # two poniter
        # res = float("inf")
        # l = 0
        # r = len(nums)-1
        # while r >= l:
        #     if nums[r] < nums[l]:
        #         res = min(nums[r], res)
        #         l += 1
        #     else:
        #         res =min(nums[l], res)
        #         r-=1
        # return res

        #O(logn)
        res = nums[0]
        r, l = len(nums)-1, 0
        while l <= r:
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break
            m = (r+l)//2 #find the midpoint
            res = min(res, nums[m])
            if nums[m] >= nums[l]: # if the midpoint num is greater that the number at the begng it means the min value is to the right side
                l = m+1
            else: #if midpoint num is not greater than the num at l focus on the left
                r = m-1
        return res

        