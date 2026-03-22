class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        #Brute Force
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] == nums[j] and abs(i - j) <= k:
        #             return True
        # return False

        seen = {}
        for i, n in enumerate(nums):
            if n not in seen:
                seen[n] = i
            elif n in seen and abs(seen[n] - i) <= k:
                return True
            else:
                seen[n] = i
        return False



        