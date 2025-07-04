class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, i):
        self.queue.append(i)

    def dequeue(self):
        if not len(self.queue):
            print("Queue is Empty. Cannot Deque.")
            return 
        
        return self.queue.pop(0)
    
    def size(self):
        return len(self.queue)
    
    def is_empty(self):
        return len(self.queue) == 0
    
    def front(self):
        return self.queue[0]
    
    def rear(self):
        return self.queue[-1]
    
if __name__ == "__main__":
    q = Queue()
    print(q.is_empty())
    q.enqueue(5)
    print(q.front())
    q.enqueue(6)
    q.enqueue(7)
    print(q.dequeue())
    print(q.dequeue())
    q.enqueue(8)
    q.enqueue(9)
    print(q.rear())
    print(q.size())
    print(q.front())
    print()