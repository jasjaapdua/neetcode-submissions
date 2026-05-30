class MinStack:

    def __init__(self):
        self.elements = []
        self.minStack = []

    def push(self, val: int) -> None:
        if not self.elements:
            self.elements.append(val)
            self.minStack.append(val)
        else:
            self.elements.append(val)
            self.minStack.append(min(self.minStack[-1], val))

    def pop(self) -> None:
        self.elements.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.elements[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
