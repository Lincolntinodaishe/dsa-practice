class Solution:
    def isValid(self, s: str) -> bool:
        pairs ={
            ')':'(',
            '}':'{',
            ']':'['
        }
        stack = []
        for char in s:
            if char in '({[':
                stack.append(char)
            if char in')]}':
                if not stack or stack[-1] != pairs[char]:
                    return False
                stack.pop()
        return not stack

        # (not stack)simply means empty stack and retuens bool true if it is empty
        