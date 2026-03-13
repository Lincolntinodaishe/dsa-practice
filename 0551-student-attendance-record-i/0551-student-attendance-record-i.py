class Solution:
    def checkRecord(self, s: str) -> bool:
        d = {
        }  
        for i in s:
            d[i] = d.get(i, 0)+1
        if "A" in d and d['A'] > 1:
            return False
        if 'LLL' in s:
            return False
        else:
            return True
        