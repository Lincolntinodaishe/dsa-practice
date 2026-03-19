class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        s = {}
        cnt = float('inf')
        res =[]
        for i, n in enumerate(list2):
            s[n] = i
        for i, n in enumerate(list1):
            if n in s:
                tot = i + s[n]
                if tot < cnt:
                    cnt = tot
                    res = [n]
                elif tot == cnt:
                    res.append(n)
        return res
                


        