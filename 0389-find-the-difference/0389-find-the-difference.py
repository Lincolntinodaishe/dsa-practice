class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        # use the differnce in ASCII values
        st,ss = 0, 0
        for i in t:
            st += ord(i)
        for i in s:
            ss += ord(i) 
        return chr(st-ss)

        