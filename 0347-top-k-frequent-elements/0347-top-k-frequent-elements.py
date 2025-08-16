class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        Buck =[[] for i in range (len(nums)+1)]
        dic = {}
        for i in nums:
            dic[i] = dic.get(i, 0)+1
        for n, c in dic.items():
            Buck[c].append(n)
        ret = []
        for i in range(len(Buck)-1, 0,-1):
            for c in Buck[i]:
                ret.append(c)
                if len(ret) == k:
                   return ret
