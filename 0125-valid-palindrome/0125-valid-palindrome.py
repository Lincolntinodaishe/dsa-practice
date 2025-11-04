class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        s = s.lower()
        b = ""
        for i in s:
            if i.isalnum():
                b += i
        return b == b[::-1]


