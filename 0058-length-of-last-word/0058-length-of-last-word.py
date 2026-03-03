class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        lst1 = s.split() # split remove spaces and creates a list of individual words in a string
        return len(lst1[-1])
        