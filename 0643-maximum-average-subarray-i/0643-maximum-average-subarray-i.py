class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # first window the move to the rest
        total = sum(nums[:k])
        avg = total/k
        l = 0
        for r in range(k, len(nums)):
            total += nums[r]
            total -= nums[l]
            curr_avg = total/k
            avg = max(avg, curr_avg)
            l += 1
        return avg

        #fixed sliding window

            
        