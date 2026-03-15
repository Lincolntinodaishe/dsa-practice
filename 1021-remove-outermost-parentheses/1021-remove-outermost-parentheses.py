class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        stack = []
        res =""

        for i in s:
            if i == '(':
                if len(stack) >0:
                    res += i
                stack.append(i)
            else:
                stack.pop()
                if len(stack) > 0:
                    res += i
        return res

        #space O(n)
        # time o(n)
        