class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        #slicing method
        seen, res = set(), set()
        for i in range(len(s)-9):
            sub = s[i:i+10]
            if sub in seen:
                res.add(sub)
            else: seen.add(sub)
        return list(res)

        #sliding window

        '''
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
        '''
