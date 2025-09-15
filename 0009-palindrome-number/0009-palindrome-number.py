class Solution:
    def isPalindrome(self, x: int) -> bool:
        # convert the interger to a string and iterate through each and every value  in the str and compare
        x = str(x)
        l = 0
        r = len(x)-1
        while l < r:
            if x[l] != x[r]:
                return False
            l += 1
            r -=1
        return True