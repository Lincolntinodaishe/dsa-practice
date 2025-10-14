class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # slow pointer: position to place the next unique element
        l = 1
        # fast pointer: scans the array from the second element
        for r in range(1, len(nums)):
            # check if current element is different from the previous (unique)
            if nums[r] != nums[r-1]:
                 # place the unique element at index l
                nums[l] = nums[r]
                # move pointer
                l +=1
            else: continue
        return l # l becomes the lenght of the unique elements

