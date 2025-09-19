class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        # we implement a stack to store the character and count. easy to add and optimal to remove when we reach our count
        stack = []
        for c in s:
            # if stack and the alst character is equal to the curr char we want to increase count
            if stack and stack[-1][0] == c:
                stack[-1][1] += 1
            else: # if the stack is empty or we are on a new char
                stack.append([c,1])
                # if our count is is equal to k during iteration we want to pop the char
            if stack[-1][1] == k:
                stack.pop()
        res = ''
        for c in stack:
            res += (c[0]*c[-1]) # we want to append the exact charcaters left and we multiply by their count
        return res