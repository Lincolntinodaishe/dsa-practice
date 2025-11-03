class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #Brute

    # n = len(s)
    # max_len = 0

    # for i in range(n):  # start index
    #     for j in range(i, n):  # end index
    #         substring = s[i:j+1]
    #         if len(set(substring)) == len(substring):  # all unique
    #             max_len = max(max_len, len(substring))
    # return max_len

        store = set()
        l =0
        res=0
        for i in range(len(s)):
            while s[i] in store:
                store.remove(s[l])
                l+=1
            store.add(s[i])
            res = max(res, i-l+1)
        return res