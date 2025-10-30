class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        dict1 ={}
        dict2 = {}
        res = float("inf") #want to compare with infinity to deal with the least number of chars in s
        if len(target) > len(s):
            return 0
        for i in target:
            dict1[i] = dict1.get(i, 0)+1
        for j in s:
            dict2[j] = dict2.get(j,0)+1
        for key, value in dict1.items():
            if dict2.get(key, 0) >= value:
                res = min(res, dict2.get(key, 0)//value )    # divide // by the value to get the number of times the least available char appears in the target
            else:
                return 0
        return res
