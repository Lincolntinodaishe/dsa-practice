class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        # convert into lists
        res = []
        carry = 0
        i = len(num1)-1
        j = len(num2)-1
        while i>=0 or j>=0 or carry:
                val1 = int(num1[i]) if i>=0 else 0
                val2 = int(num2[j]) if j>=0 else 0
                total = val1 + val2 + carry
                val = total%10
                carry = total//10
                res.append(str(val))
                i -= 1
                j -= 1
        return "".join(res[::-1])        
    
