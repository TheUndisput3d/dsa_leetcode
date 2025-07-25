def printName(n, name):
  if n == 0:
    return 
  
  print(name)
  printName(n-1, name)


def f(i, n):
  if i > n:
    return
  
  print("Aayush")
  f(i+1, n)

if __name__ == "__main__":
  n = int(input("Enter any n: "))
  f(1, n)