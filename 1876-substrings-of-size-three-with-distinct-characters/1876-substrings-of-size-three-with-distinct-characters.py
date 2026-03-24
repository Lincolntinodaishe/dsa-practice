class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        arr = []
        l = 0
        count = 0
        for r in range(len(s)):
            arr.append(s[r])
            if r -l+1 > 3:
                arr.remove(s[l])
                l+=1
            if r-l+1 == 3 and len(set(arr)) == 3:
                count += 1 
        return count       