class MinStack:

    def __init__(self):
        self.stack = []
        self.min = []

    def push(self, val: int) -> None:
        self.stack.append(val)

        if(self.min and val > self.min[-1]):
            self.min.append(self.min[-1])
        else:
            self.min.append(val)


    def pop(self) -> None:
        if self.stack:
            self.stack.pop()
            self.min.pop()
        

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]
        

    def getMin(self) -> int:
        if self.min:
            return self.min[-1]