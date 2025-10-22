class Solution:
    def longestPalindrome(self, s: str) -> int:
        # it is case sensetive so do not change the cases
        total = 0  
        dict1 = {}
        odd_count = False # create an odd_count tracker 
        for i in s:
            dict1[i] = dict1.get(i, 0)+1 # add characters and their freq
        for count in dict1.values(): # iterate through out the values
            if count%2 == 0:   #Iif count is even then the chars can make a palindrome
                total += count
            elif count%2 != 0: # if count is odd we want that value -1 (this ensures that the ones we add are subtracteed)
                total += count-1  
                odd_count = True # since we have an odd count update to true
        if odd_count: 
            return total + 1 # if true add one cause one letter can be put in the middle of a palindrome and still pake it valid 
        return total # if not just return the total
