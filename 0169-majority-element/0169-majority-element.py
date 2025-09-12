class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        Ndic = {}
        for i in nums:
            Ndic[i] = Ndic.get(i, 0)+1
            if Ndic[i] > len(nums)/2:
                return i