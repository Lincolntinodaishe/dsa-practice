class Solution:
    def reverseWords(self, s: str) -> str:
        res = []
        s = s.split() # splits words in a string using the space sperator into a list of individual words
        for word in s:
            res.append(word[::-1])
        return ' '.join(res)