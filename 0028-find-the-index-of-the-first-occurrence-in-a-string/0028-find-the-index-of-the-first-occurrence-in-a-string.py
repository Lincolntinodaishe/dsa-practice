class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        '''
        use 2 pointers
        l - hay
        r - need
        search hay and need
        if the pointers have the same value
        move to the next
        if not keep the hay pointer wher it is and move needle
         pointer back to zero

        '''
        index = 0
        l = 0
        r = 0
        while l<len(haystack) and r<len(needle):
            if haystack[l] ==  needle[r]:  
                
                if r == len(needle)-1: #when we reach the last word in the needle return inde
                    return l-r
                l+=1 #update pointers
                r+=1
                
            else:  #if pointers are not equal, restart the needle and move the haystack
                l= l-r+1
                r = 0
        return -1 # ifyou get out of the loop without finding anything return -1

        