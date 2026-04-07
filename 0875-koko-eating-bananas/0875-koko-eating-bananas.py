class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        import math
        '''
        koko can eat k bananas per hour
        to finish each pile inone hour koko should eat at k = max(pile)
        there4 the min num of hours she can do is  len(pile) to fin the whole pile
        so this means that if h == 5 and len(piles) == 5 then k == max(piles)
        if h > 5 and len(pile)== 5 then k is less than max(pile)
        basically given any valid h, k = [1...max(piles)]
        use binary search to test every number and return the min val ok k that satisfies h 
        '''

        if h == len(piles):
            return max(piles)

        l , r = 1, max(piles)
        res = float('inf')
        while l<=r:
            mid = (l+r)//2
            count = 0
            for i in piles:
                count += math.ceil(i/mid) # cal the hours when k = mid
            if count <= h: # if hours are <= h we continue looking for the min k
                res = min(res, mid)
                r = mid-1
            else:
                l = mid +1
        return res
