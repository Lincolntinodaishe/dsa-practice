class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # we want to sort the intervals by comparing the startin number of each interval
        intervals.sort(key=lambda x:x[0])
        merged = []
        for interval in intervals:
            # if the merged is empty we want to add the first interval.
            # if we add the first and it wont merge with the lates interval, we just want to add the interval
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            # if the merge we want the last value in the merged to be the maximum between itself and the last value in the interval
            else:
                merged[-1][1] = max(merged[-1][1], interval[1])
        return merged