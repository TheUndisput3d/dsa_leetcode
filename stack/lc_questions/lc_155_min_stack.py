class MinStack:

    def __init__(self):
        self.items = []

    def push(self, val: int) -> None:
        if not len(self.items):
            self.items.append([val, val])
        else:
            curr_min = min(self.items[-1][1], val)
            self.items.append([val, curr_min])


    def pop(self) -> None:
        self.items.pop() 

    def top(self) -> int:
        return self.items[-1][0]
        

    def getMin(self) -> int:
        return self.items[-1][1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()