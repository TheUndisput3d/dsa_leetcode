from ..binary_tree_implem import Node

def preorder(node):
  if node == None:
    return
  
  print(node.data, end=" ")
  preorder(node.left)
  preorder(node.right)


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

  preorder(drinks)

