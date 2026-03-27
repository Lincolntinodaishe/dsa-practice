class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        '''
        res =[]
        set1 = set(nums1)
        for i in nums2:
            if i in set1:
                res.append(i)
        return list(set(res)) 
        '''
        #set0.intersection(set1, set2) - set function
        return list(set(nums1).intersection(set(nums2)))

        

        