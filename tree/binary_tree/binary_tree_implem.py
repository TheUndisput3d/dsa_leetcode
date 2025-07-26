class Node():
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None

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

  print(hot.right.data)
  print(cold.right.data)
  print(drinks.data)
  print(drinks.left.left.data)
  print(drinks.right.right.data)
  print(drinks.right.left.data)
  # print(drinks.right.right.left.right) # Attribute error as None as no left or right attribute>>>>