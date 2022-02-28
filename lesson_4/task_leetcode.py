class MinStack:

    def __init__(self):
        self.stack = []
        self.min = []

    def push(self, x) -> None:
        self.stack.append(x)

        if not self.min or x <= self.min[-1]:
            self.min.append(x)

    def pop(self) -> None:
        if not self.stack:
            return None

        el = self.stack.pop()

        if el == self.min[-1]:
            self.min.pop()
            return el

    def top(self) -> int:
        if not self.stack:
            return None
        return self.stack[-1]

    def getMin(self) -> int:
        if not self.min:
            return None
        return self.min[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()


