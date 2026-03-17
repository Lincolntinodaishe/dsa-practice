class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        d = {}
        sec = 0
        for i, n in enumerate(tickets):
            d[i] = n
        while d[k] > 0:
            for i in range(len(tickets)):
                if d[i] > 0:
                    d[i] = d.get(i, 0)-1
                    sec +=1
                if d[k] == 0:
                    return sec
        return sec

        # time o(n)