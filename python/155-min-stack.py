class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.minIndex = -1
        self.topIndex = -1

    def push(self, x: int) -> None:
        self.stack.append(x)
        self.topIndex += 1
        if(self.topIndex > 0):
            self.minIndex = self.minIndex if(self.stack[self.minIndex] <= self.stack[self.topIndex]) else self.topIndex
        elif(self.topIndex == 0):
            self.minIndex = 0
        else:
            self.minIndex = -1
        return
    
    def pop(self) -> None:
        if(self.topIndex < 0):
            return

        self.stack.pop()

        if(self.topIndex == 0):
            self.minIndex = -1
            
        if(self.minIndex == self.topIndex):
            self.minIndex = 0
            for i in range(1, self.topIndex):
                if(self.stack[i] < self.stack[self.minIndex]):
                    self.minIndex = i
        self.topIndex-=1
        return

    def top(self) -> int:
        if(self.topIndex<0): return None
        return self.stack[self.topIndex]

    def getMin(self) -> int:
        if(self.minIndex == -1): return None
        return self.stack[self.minIndex]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()