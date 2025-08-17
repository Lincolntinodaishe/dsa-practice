class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        dic1 = {}
        dic2 = {}
        for i in s:
            dic1[i]=dic1.get(i, 0) +1
        for e in t:
            dic2[e]=dic2.get(e, 0)+1
        for key in dic1:
            if dic1[key] != dic2.get(key, 0):
                return False
        return True
                
                
           