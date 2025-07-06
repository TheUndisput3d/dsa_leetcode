from collections import deque

class StackUsingQueue:
  def __init__(self):
    self.queue = deque()

  def push(self, item):
    self.queue.append(item)
    n = len(self.queue)
    
    for i in range(n-1): 
      self.queue.append(self.queue.popleft())

  def pop(self):
    if len(self.queue) == 0:
      return "The Stack is empty."
    return self.queue.popleft()
  
  def peek(self):
    if len(self.queue) == 0:
      return "The Stack is empty."
    return self.queue[0]
  
  def is_empty(self):
    return len(self.queue) == 0
  
  def size(self):
    return len(self.queue)
  
  def traverse(self):
    return self.queue

if __name__ == "__main__":
  s = StackUsingQueue()
  s.push(5)
  s.push(7)
  print(s.traverse())
  s.push(8)
  print(s.traverse())
  print(s.peek())
  print(s.pop())
  print(s.pop())

  