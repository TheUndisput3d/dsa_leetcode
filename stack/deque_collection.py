from collections import deque

# Deque helps to append and pop from both rear and front with O(1) Time Complexity

if __name__ == "__main__":

  lst = deque([])

  lst.append(5)
  lst.append(6)
  lst.append(7)
  lst.append(8)
  lst.appendleft(9)
  lst.appendleft(10)

  print(lst)

  lst.pop()
  print(lst)
  lst.popleft()
  print(lst)

