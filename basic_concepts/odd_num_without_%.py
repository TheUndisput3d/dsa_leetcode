def isEven(num):
  ans = True
  
  for i in range(num):
    ans = not ans
  
  return ans

def isOdd(num):
  ans = True
  
  for i in range(num):
    ans = not ans

  return not ans

def isOdd2(num):
  ans = True
  
  for i in range(num):
    ans = not ans

  return not ans

if __name__ == "__main__":
  print(isEven(28))
  print(isOdd(23))
  print(isOdd2(23))
