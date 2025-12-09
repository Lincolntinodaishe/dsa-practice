class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        total = sum(apple)
        capacity.sort(reverse=True)
        nums= 0
        count = 0

        for i in capacity:
            nums += i
            count += 1
            if total <= nums:
                return count
            



        