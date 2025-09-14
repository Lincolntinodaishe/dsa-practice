class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # the length limitation
        if len(ransomNote) > len(magazine):
            return False
        dict1 ={}
        dict2 = {}
        for i in ransomNote:
            dict1[i] = dict1.get(i, 0)+ 1
        for j in magazine:
            dict2[j] = dict2.get(j, 0)+1
        
        for key, value in dict1.items():
            if dict2.get(key, 0) < value: # if key not in dict2 or dict2[char] < count:
                return False
            
        return True