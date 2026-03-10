class Solution:
    def frequencySort(self, s: str) -> str:
        d = {}
        res =''
        for i in s:
            d[i] = d.get(i, 0)+1
        # sorting a dict with lambda function
        
        sd = dict(sorted(d.items(), key=lambda x: x[1], reverse = True))
        for k, v in sd.items():
            res += k*v
        return res
        