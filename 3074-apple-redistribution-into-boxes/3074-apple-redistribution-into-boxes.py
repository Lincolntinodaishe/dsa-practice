class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        total = sum(apple)
        capacity.sort(reverse=True)
        

        for i, item in enumerate(capacity):
            if total > 0:
                total -= item
            else: return i
        return i+1
            



        