class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        key = ''
        res = []
        d = {}
        l = 0
        for r in range(len(s)):
            key += s[r]
            if r-l+1 >10:
                key = s[l+1:r+1]
                l+=1
            if r-l+1 == 10:
                d[key] = d.get(key, 0)+1
        for i in d:
            if d[i] > 1:
                res.append(i)
        return res
        #slide a fixed window of len 10 and hash