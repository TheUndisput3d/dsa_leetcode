class Stack:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        return len(self.stack) == 0
    
    def top(self):
        return self.stack[-1]
    
    def append(self, i):
        self.stack.append(i)
    
    def pop(self):
        if not len(self.stack):
            print("Stack is Empty. Cannot Pop")
            return 
        return self.stack.pop()

    def size(self):
        return len(self.stack)
    
if __name__ == "__main__":
    a = Stack()
    a.append(5)
    a.append(6)
    print(a.top())
    print(a.is_empty())
    a.append(7)
    print(a.top())
    a.pop()
    a.pop()
    a.pop()
    print(a.is_empty())
