class Solution:
    def longestPalindrome(self, s: str) -> str:
        # we have two main cases when our palindrome is even odd
        # we want to check each ane every possible combination of adjacent chars
        # return the longest palindromic substring
        # store the substring
        # store the length and use it to compaper
        # two pointers

        # brute force will be to check each and every combinatiob using for loops
        # then check if palindrome, compare lenght and return the substr
        # but time complexity O(n^2)

        res = ''
        res_len = 0
        # when the len of s id odd
        for i in range(len(s)):
            l = i      #your pinters must begin at the same position moving out
            r = i
            while l>=0 and r <len(s) and s[l] == s[r]:  # checks  range and palindromic status
                if res_len < r-l+1 : #if curr lenght is less than what we have
                    res = s[l:r+1]   # update the substring 
                    res_len = r-l+1  # update the new lenght
                l -= 1               # move your pointrs
                r += 1
        # when the length is even
        for i in range (len(s)):
            l = i      # the rtight pointer must be in front of the left
            r = i+1
            while l>=0 and r <len(s) and s[l] == s[r]:
                if res_len < r-l+1 :
                    res = s[l:r+1]
                    res_len = r-l+1
                l -= 1
                r += 1
        return res # return results
            
            