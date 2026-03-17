class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        for i in s:
            if stack and (stack[-1].isupper() and i.islower()) and stack[-1].lower() == i:
                stack.pop()
            elif stack and (stack[-1].islower() and i.isupper()) and i.lower() == stack[-1]:
                stack.pop()
            else:
                stack.append(i)
        return ''.join(stack)

        