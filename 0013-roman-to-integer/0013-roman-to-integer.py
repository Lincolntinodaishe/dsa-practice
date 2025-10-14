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
        # reverse the string
        # s = s[::-1]
        # loop upto the char before the last one because you cant compare after that as you will be out of range
        # for i in range(0, len(s)-1):
        #     if s[i] == 'V' and s[i+1] == 'I':
        #         res += 3
        #     elif s[i] == 'X' and s[i+1] == 'I':
        #         res += 8
        #     elif s[i] == 'L' and s[i+1] == 'X':
        #         res += 30
        #     elif s[i] == 'C' and s[i+1] == 'X':
        #         res += 80
        #     elif s[i] == 'D' and s[i+1] == 'C':
        #         res += 300
        #     elif s[i] == 'M' and s[i+1] == 'C':
        #         res += 800
        #     else:
        #         res += dict1[s[i]]
        # remember to add the last character after the loop
        # res += dict1[s[-1]]
        # return res

        # you dont need to reverse your string
        # understand that if my current roman numeral is less than the one in front
        # i have to subtract it
        # you access evry char but the last because you dont what to go out of range when comparing the last cha
        for i in range(len(s)-1):  
            if dict1[s[i]] < dict1[s[i+1]]:
                res -= dict1[s[i]]
            else:
                res += dict1[s[i]]
         # add your last element to the result   
        res += dict1[s[-1]]
        return res