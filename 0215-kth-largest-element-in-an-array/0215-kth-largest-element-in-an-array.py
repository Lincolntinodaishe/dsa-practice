import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # # O(nlogn)
        # nums.sort()
        # return nums[len(nums)-k] 

        # min heap
        min_heap = []  # create a heap srorage
        for i in nums:
            if len(min_heap)< k: # add restrictions to the leng of the heap
                heapq.heappush(min_heap, i) # adding values until the heap has k items
            else:
                heapq.heappushpop(min_heap, i) # otherwise pudh a large number at the bottom then pop the top least number
        return min_heap[0] # the number at the top is the the k largest then return it