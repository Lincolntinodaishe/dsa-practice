class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        import operator
        d = {
            '+': operator.add,
            '-': operator.sub,
            '*': operator.mul,
            '/': operator.truediv
         }
        stack = []
        for token in tokens:
            if token in "+-*/":
                if token == '/':
                    val = int(stack[-2]/stack[-1])
                else:
                    val = d[token](stack[-2], stack[-1])
                stack.pop()
                stack.pop()
                stack.append(val)
            else:
                stack.append(int(token))
        return stack[0]
        
'''
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        import operator
        stack = []
        operators = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv
    }
        for token in tokens:
            if token.isdigit() or (token[0] == '-' and token[1:].isdigit()):
                stack.append(int(token))
            else:
                b = stack.pop()
                a = stack.pop()
                if token == '/':
                    stack.append(int(a/b))
                else:
                    stack.append(operators[token](a, b))
        return int(stack[0])

        #Python’s / operator (operator.truediv) always returns a float.
#LeetCode’s RPN problem usually expects integer division that truncates toward zero.

#Example:

#-7 / 3       # Python float division → -2.333...
#int(-7 / 3)  # truncates → -2


#LeetCode expects: -7 / 3 → -2 ✅ (good here)

#But sometimes people do floor division with //:

-7 // 3      # -3 ❌
'''
        

        