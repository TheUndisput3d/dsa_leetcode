class Node:
    def __init__(self, val):
        self.prev = None
        self.next = None
        self.val = val

class QueueUsingDLL:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, val):
        new_node = Node(val)
        if not self.head:
            self.head = new_node
            self.tail = self.head

        self.tail.next = new_node
        new_node.prev = self.tail
        self.tail = new_node

    def dequeue(self):
        if not self.head:
            return "The Queue is Empty."
        if self.head == self.tail:
            to_del = self.head
            self.head = self.tail = None
            return to_del.val

        self.head.next.prev = None
        deleted_node = self.head
        self.head = self.head.next
        deleted_node.next = None
        return deleted_node.val
    
    def is_empty(self):
        return self.head == None


if __name__ == "__main__":
    s = QueueUsingDLL()
    s.enqueue(2)
    s.enqueue(3)
    s.enqueue(5)
    s.enqueue(7)
    print(s.dequeue())
    print(s.dequeue())
    print(s.dequeue())
    print(s.dequeue())
    print(s.is_empty())


    

    


