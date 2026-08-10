class MinStack:

    def __init__(self):
        self.stack = []
        self.minHistory = []

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append(val)
            self.minHistory.append(val)
        else:
            self.stack.append(val)
            self.minHistory.append(min(val, self.minHistory[-1]))

    def pop(self) -> None:
        self.stack.pop()
        self.minHistory.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minHistory[-1]
        
