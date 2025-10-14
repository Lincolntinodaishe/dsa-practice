class Solution:
    def romanToInt(self, s: str) -> int:
        dict1 = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        res = 0
        s = s[::-1]
        for i in range(0, len(s)-1):
            if s[i] == 'V' and s[i+1] == 'I':
                res += 3
            elif s[i] == 'X' and s[i+1] == 'I':
                res += 8
            elif s[i] == 'L' and s[i+1] == 'X':
                res += 30
            elif s[i] == 'C' and s[i+1] == 'X':
                res += 80
            elif s[i] == 'D' and s[i+1] == 'C':
                res += 300
            elif s[i] == 'M' and s[i+1] == 'C':
                res += 800
            else:
                res += dict1[s[i]]
        res += dict1[s[-1]]
        return res