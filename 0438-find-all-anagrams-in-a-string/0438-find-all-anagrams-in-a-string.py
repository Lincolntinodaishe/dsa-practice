class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # first conditon is if len of p is > that of s
        if len(p) > len(s):
             return []
        dict1 = {}
        dict2 = {}
        res=[]
        l = 0

        # for my first window that has the same leng to p
        for i in range(len(p)):
            dict2[p[i]]=dict2.get(p[i], 0)+1
            dict1[s[i]]=dict1.get(s[i], 0)+1
        if dict1 == dict2:
            res = [0]

        # for the rest of s, as r iterates from len(p) to the end of s
        # decrease the s[l] char in the dictionary anfd if zero remove it
        # increament l pointer to manatin the window len
        for r in range(len(p), len(s)):
            dict1[s[r]] = dict1.get(s[r], 0)+1
            dict1[s[l]] -= 1
            if dict1[s[l]] == 0:
                dict1.pop(s[l])
            l+=1
        # compare the two dicts if they match take the index l and append it to res
            if dict1 == dict2:
                res.append(l)
        return res
        