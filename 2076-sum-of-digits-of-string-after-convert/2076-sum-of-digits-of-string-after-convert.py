class Solution:
    def getLucky(self, s: str, k: int) -> int:
        # we used a while loop to track k , when k nis 0 or les we break the loop
        # ord('a') is 97
        # res to be brought to zero everytime after we update word
        # then decerase k 
        res = 0
        word = ""
        for i in s:
            word += str(ord(i)-96)
        while k > 0:
            for j in word:
                res += int(j)
            word =  str(res)
            res = 0
            k-= 1
        return int(word) 
            
    