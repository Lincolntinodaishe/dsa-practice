class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        # since arrays are not immutable we want to create a list of the chars
        # make it mutable
        res = []
        # now we loop at intervals that are 2*k long
        # for eg 1 this is from a to d
        for i in range(0, len(s), 2*k):
            # for the first k chars we want to reverse them. so we append the then reverse them
            res.append(s[i:i+k][::-1])
            # for the rest of the terms in the interval we just append them
            res.append(s[i+k:i+2*k])
        # we join the items in the list to a string
        return "".join(res)