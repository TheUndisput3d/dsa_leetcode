# Implementation of a queue using 2 stacks.

class QueueUsingStacks:
  def __init__(self):
    self.stk1 = []
    self.stk2 = []

  def enqueue(self, item):
    while self.stk1:
      self.stk2.append(self.stk1.pop())
    self.stk1.append(item)
    while self.stk2:
      self.stk1.append(self.stk2.pop())

  def dequeue(self):
    if self.is_empty():
      return "The stack is empty."
    return self.stk1.pop()
  
  def front(self):
    return self.stk1[-1]
  
  def is_empty(self):
    return not self.stk1
  
  def size(self):
    return len(self.stk1)
  


if __name__ == "__main__":
  q = QueueUsingStacks()
  q.enqueue(5)
  q.enqueue(6)
  q.enqueue(8)
  print(q.dequeue())
  print(q.dequeue())
  print(q.size())
  print(q.dequeue())
  print(q.is_empty())