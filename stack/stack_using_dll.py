class Node:
    def __init__(self, val):
        self.prev = None
        self.next = None
        self.val = val

class StackUsingDLL:
    def __init__(self):
        self.head = None
        self.tail = None

    def push(self, val):
        new_node = Node(val)
        if not self.head:
            self.head = new_node
            self.tail = self.head

        self.tail.next = new_node
        new_node.prev = self.tail
        self.tail = new_node

    def pop(self):
        if not self.head:
            return "The Stack is Empty."
        
        elif self.head == self.tail:
            to_del = self.head
            self.head = self.tail = None
            return to_del.val
            
        self.tail.prev.next = None
        delted_node = self.tail
        self.tail = self.tail.prev
        delted_node.prev = None
        return delted_node.val
    
    def is_empty(self):
        return self.head == None


if __name__ == "__main__":
    s = StackUsingDLL()
    s.push(2)
    s.push(3)
    s.push(5)
    s.push(7)
    print(s.pop())
    print(s.pop())
    print(s.pop())
    print(s.pop())
    print(s.is_empty())


    

    


