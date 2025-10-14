class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # control i manually by using a while loop
        # exchange the numbers with the last one uing python exchange
        # and move the pointer
        i =0
        while i < len(nums):
            if nums[i] == val:
                nums[i], nums[-1] = nums[-1], nums[i]
                nums.pop()
            else:
                i+=1
        return len(nums)