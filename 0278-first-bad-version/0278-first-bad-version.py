# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        # check if mid is bad 
        # if not l = mid+1
        # if it is we go down r = mid-1
        l =0
        r =n
        while l<=r:
            mid = (l+r)//2
            if not isBadVersion(mid):
                l = mid+1
            else:
                r = mid-1

        return l

        