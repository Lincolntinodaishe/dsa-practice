class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        dic = {}
        dic2 = {}

        for char in s:
            dic[char] = dic.get(char, 0) + 1
        
        for char in t:
             dic2[char] = dic2.get(char, 0) + 1
        
        for key in dic:
            if dic[key] != dic2.get(key, 0):
                return False
            
        return True