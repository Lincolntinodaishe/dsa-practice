class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for i in operations:
            if (i.lstrip('-')).isdigit(): #function .lstrip us for negative integers to be tested .isdigit
                stack.append(int(i))
            elif i == '+':
                stack.append(stack[-1] + stack[-2])
            elif i == 'D':
                stack.append(2*stack[-1])
            elif i == 'C':
                stack.pop()
        return sum(stack)