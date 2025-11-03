class Solution:
    def mySqrt(self, x: int) -> int:
        if x<2:
            return x
        ans = 0
        l = 0
        r = x
        while l <= r:
            m = (l+r)//2
            if m * m == x:
                return m
            elif m * m < x:
                ans = m # store m as the largest integer that can be squared to give a value less than x
                l = m+1
            else:
                r = m-1 
        return ans
        # binarry search