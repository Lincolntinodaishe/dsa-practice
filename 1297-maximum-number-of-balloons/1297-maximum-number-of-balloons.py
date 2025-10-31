class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        res = float("inf")
        dict1 ={}
        dict2 = {}
        target = "balloon"
        if len(text)<len(target):
            return 0
        # len differnce
        #store balloon and text 2 diff dicts
        # get function
        # to get the keys in the balloon dict from dict of text and compare to the values of the balloon
        # if freq > value 
        # upate res to the minimun value between itself and freq fro th get
        for i in target:
            dict1[i] = dict1.get(i, 0)+1
        for j in text:
            dict2[j] = dict2.get(j, 0)+1
        for key, value in dict1.items():
            if dict2.get(key, 0) >= value:
                res =min(res, dict2.get(key, 0)//value)
            else:
                return 0
        return res


        