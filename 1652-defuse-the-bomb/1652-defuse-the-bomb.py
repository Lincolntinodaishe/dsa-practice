class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        '''
        sliding window
        circular array use modulo
        code = [5,7,1,4], k = 3
        since the last number has to be added to the three next number
        the circular arr = code = [5,7,1,4,5,7,1], coz we added k spots (k = 3)
        we use mod to keep track of the actual index in code arr, eg the second 5 would be at 4%4 whc is= 0
        '''
        N = len(code)
        res = [0]*N
        curr_sum = 0
        l =0
        for r in range(N + abs(k)):
            curr_sum += code[r%N] # use abs cause k can be neg
            if r+1-l > abs(k):
                curr_sum -= code[l%N]
                l = (l+1)%N
            if r+1-l == abs(k):
                if k > 0: # if k is positive look at the number before l
                    res[(l-1)%N] = curr_sum
                if k < 0: # if k is neg look at the value after r
                    res[(r+1)%N] = curr_sum
        return res
        

        