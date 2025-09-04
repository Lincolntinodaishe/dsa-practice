class MinStack:

    def __init__(self):
        self.mainStack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.mainStack.append(val)
        if not self.minStack:
            self.minStack.append(val)
        else:
            self.minStack.append(min(val, self.minStack[-1]))
        

    def pop(self) -> None:
        self.mainStack.pop()
        self.minStack.pop()
    def top(self) -> int:
        return self.mainStack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
# one stack for the minimums and Another for the normal pushes.
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()