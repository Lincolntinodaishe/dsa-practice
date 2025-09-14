class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # if the lengths of the strings are different , anagram is false
        if len(s) != len(t):
            return False
        # best storage with an o(1) look
        dict1 ={}
        dict2= {}
        # into the dictionaries
        for i in s:
            dict1[i] = dict1.get(i, 0)+1
        for j in t:
            dict2[j] = dict2.get(j, 0)+1
        #Compare the dictionaries
        if dict1 != dict2:
            return False
        return True
                  
  
           