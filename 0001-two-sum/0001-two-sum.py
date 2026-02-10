class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # #brute
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i,j]
        #         else:
        #             continue

        #optimal
        dict1 = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in dict1:
                return [dict1[diff], i]
            else:
                dict1[n] = i

