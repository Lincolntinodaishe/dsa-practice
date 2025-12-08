class Solution:
    def isBalanced(self, num: str) -> bool:
        odd = 0
        even = 0
        n = len(num)

        for i in range(0, n, 2):
            even += int(num[i])
        for i in range(1, n, 2):
            odd += int(num[i])

        return odd == even


        