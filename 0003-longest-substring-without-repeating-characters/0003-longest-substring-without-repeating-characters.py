class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        C = set()
        l =0
        res = 0
        for r in range(len(s)):
            while s[r] in C:
                C.remove(s[l])
                l += 1
            res = max(res, r - l+1)
            C.add(s[r])
        return res
