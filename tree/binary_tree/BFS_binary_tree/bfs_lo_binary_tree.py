from collections import deque
from ..binary_tree_implem import Node

def bfs_traversal(node):
  queue = deque([])
  queue.append(node)

  while len(queue) != 0:
    curr = queue.popleft()
    print(curr.data, end=" ")

    if curr.left is not None:
      queue.append(curr.left)

    if curr.right is not None:
      queue.append(curr.right)

if __name__ == "__main__":
  drinks = Node("drinks") 
  hot = Node("hot") 
  cold = Node("cold") 
  tea = Node("tea") 
  coffee = Node("coffee") 
  cola = Node("cola") 
  fanta = Node("fanta") 

  drinks.left = hot
  hot.left = tea
  hot.right = coffee
  cold.left = cola
  cold.right = fanta
  drinks.right = cold

  bfs_traversal(drinks)

    


