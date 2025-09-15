class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        p =""
        for c in s:
            if c.isalnum():
                p += c 
        l =0
        r = len(p)-1
        while l < r:
            if p[l] != p[r]:
                return False
            l+=1
            r-=1
        return True