class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a = a[::-1]
        b = b[::-1]
        ret =''
        i = 0
        carry = 0
        while i<len(a) or i<len(b) or carry:
            y = a[i] if i<len(a) else 0
            x = b[i] if i<len(b) else 0
            total = int(y) + int(x) + carry
            value = total%2
            carry = total //2
            ret += str(value)
            i += 1
        return ret[::-1]
    
        
        
        