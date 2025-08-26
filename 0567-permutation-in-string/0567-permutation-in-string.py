class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        l = 0
        r = len(s1)-1
        count1 =[0]*26
        count2 =[0]*26

        for i in s1:
            count1[ord(i)-ord('a')] += 1
         # for the first window

        for u in s2[l:r+1]:
            count2[ord(u)-ord('a')] += 1
        if count1 == count2:
            return True
        # the rest of s2
        for r in range(len(s1), len(s2)):
            count2[ord(s2[r])-ord('a')] += 1
            count2[ord(s2[l])-ord('a')] -= 1
            l +=1
            if count1 == count2 :
                return True
        return False