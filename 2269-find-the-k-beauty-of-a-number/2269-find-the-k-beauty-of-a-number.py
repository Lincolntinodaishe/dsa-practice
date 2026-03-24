class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        res = 0
        l=0
        num = str(num)
        for r in range(len(num)):
            if r-l+1 > k:
                l+=1
            if r-l+1 == k:
                if int(num[l:r+1]) == 0:
                    continue
                elif int(num) % int(num[l:r+1]) == 0:
                    res += 1
                else:
                    continue
        return res
        #sliding window

        