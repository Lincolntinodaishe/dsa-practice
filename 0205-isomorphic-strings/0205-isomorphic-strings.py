class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(t) != len(s):
            return False
        dict1 = {}
        dict2 = {}
        for c1, c2 in zip(s, t):# zip allows me to iterate in two str
            if (c1 in dict1 and dict1[c1]!= c2) or (c2 in dict2 and dict2[c2] != c1) : 
                # check if a char is mapped to the same char in bot maps
                return False
            dict1[c1] = c2  # map chars 
            dict2[c2] = c1
        return True

