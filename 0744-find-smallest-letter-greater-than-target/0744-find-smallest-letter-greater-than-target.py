class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        # min_v = float('inf')
        # for i in letters:
        #     if ord(i) > ord(target):
        #         min_v = min(min_v, ord(i))
        # return chr(min_v) if min_v != float('inf') else letters[0]
        l = 0
        r = len(letters)-1
        while  l <= r:
            mid = (r+l)//2
            if letters[mid] <= (target):
                l = mid+1
            else:
                r = mid-1
        return letters[l %len(letters)]
        