class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        # convert the eelements to strings 
        for i, n in  enumerate(nums):
            nums[i] = str(n)
        # create a function that compares the combined strings 
        def compare(n1, n2):
            if n1+n2 > n2+n1: # return n1 in front
                return -1
            else:
                n2+n1 > n1+n2
                return 1   # return n2 in front if it is larger
        nums = sorted(nums, key = cmp_to_key(compare)) #to sort 
        return str(int(''.join(nums))) # return a string of intergers for the edge case where we have all zeros