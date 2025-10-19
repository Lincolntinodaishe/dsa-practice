class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        # sole like we are doing the normal addition on paper ie: start from the last number to the first
        # create a storing list
        res=[]
        # intiate carry 0
        carry = 0 
        # pointers from the end fof the strings
        i = len(num1)-1
        j = len(num2)-1
        # while loop such that it keeps runing up until bot lists are done and we had nothing to carry
        while j>=0 or i>=0 or carry > 0:
            # create condition for the strings to give 0 when the pointers are ngtv
            digit1 = int(num1[i]) if i >= 0 else 0
            digit2 = int(num2[j]) if j >= 0 else 0

            total = digit1 + digit2 + carry
            # calc the carry using // which gives the anwer with no remainder
            carry = (total // 10)
            # append the actual number we need in the result 
            res.append(str(total % 10))
            # move pointers back
            i -= 1
            j -= 1
        # since we have intergers already we now join them into a list but reversed
        return "".join(res[::-1])
