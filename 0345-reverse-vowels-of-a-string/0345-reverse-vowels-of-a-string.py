class Solution:
    def reverseVowels(self, s: str) -> str:
        d = {'a','e','i','o','u','A','E','I','O','U'}
        l, r = 0, len(s)-1
        lst  = list(s)
        while l<r:
            if lst[l] in d and lst[r] not in d:
                r-=1
            elif lst[l] not in d and lst[r] not in d:
                l+=1
                r-=1
            elif lst[l] not in d and lst[r] in d:
                l+=1
            if s[l] in d and s[r] in d:
                lst[l], lst[r] = lst[r], lst[l]
                l+=1
                r-=1
        res = ''.join(lst)
        return res
        