class MinStack:

    def __init__(self):
        self.MinStack = []
        self.ms = []

    def push(self, val: int) -> None:
        self.MinStack.append(val)
        val = min(val, self.ms[-1] if self.ms else val)
        self.ms.append(val)

    def pop(self) -> None:
        self.MinStack.pop()
        self.ms.pop()

    def top(self) -> int:
        return self.MinStack[-1]

    def getMin(self) -> int:
        return self.ms[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()