class Solution:
    def reverseWords(self, s: str) -> str:
        #one liner:
        return " ".join(s.split()[::-1])

        # # we use the split fnction that breaks the words into a list of words
        # s = s.split() #  this makes a list of every word inthe string ignoring spaces
        # # join the reversed list but with one space in between
        # return " ".join(s[::-1])
