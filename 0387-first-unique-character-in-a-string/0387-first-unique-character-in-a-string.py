class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = {}
        d2 = {}
        for n, i in enumerate(s):
            d2[i] = n
            d[i] = d.get(i, 0)+1
        for k, v in d.items():
            if v ==1:
                return d2[k]
        return -1
        