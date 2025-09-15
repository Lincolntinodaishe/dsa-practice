class Solution:
    def isPalindrome(self, s: str) -> bool:
        # s = s.lower()
        # p =""
        # for c in s:
        #     if c.isalnum():
        #         p += c 
        # l =0
        # r = len(p)-1
        # while l < r:
        #     if p[l] != p[r]:
        #         return False
        #     l+=1
        #     r-=1
        # return True

        s = s.lower()
        l = 0
        r =len(s)-1
        while l<r:
            if s[l].isalnum() and not s[r].isalnum():
                r-=1
            elif s[r].isalnum() and not s[l].isalnum():
                l+=1
            elif not s[r].isalnum() and not s[l].isalnum():
                r-=1
                l+=1
            elif (s[r].isalnum() and s[l].isalnum()) and s[l] != s[r]:
                return False
            else:
                r -=1
                l +=1
        return True