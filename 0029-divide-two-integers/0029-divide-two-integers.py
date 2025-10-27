class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend > 0 and divisor < 0: #dividing with a negative using // will floor the answer towards the lower numer eg. 10//-3 = -4 but we want -3, so make it positive then negative
            x =dividend//(-1 * divisor)
            x = -1*x
        elif dividend < 0 and divisor > 0: # if the dividend is negative it give a negative answers
            x = (-1 *dividend)//divisor
            x = -1*x
        else: x = dividend // divisor
        # conditions for the size of x
        if x > 2**31-1 :
            return 2**31-1
        elif x < -2**31:
            return -2**31
        else:
            return x
        