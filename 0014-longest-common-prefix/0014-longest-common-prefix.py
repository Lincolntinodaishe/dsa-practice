class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs = sorted(strs) # sort so that the two outer most words will be the most different
        l = strs[0] # first word
        r = strs[-1] # last word
        res = ''
        for i in range(min(len(strs[0]), len(strs[-1]))): # TRAVESE THROUGH THE LENGTH OF THE SHORTEST WORD
            if l[i] != r[i]:
                return res
            res += l[i]
        return res
        
        