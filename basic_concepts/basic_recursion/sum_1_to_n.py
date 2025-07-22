def sumNums(n, sum_):
  if n == 0:
    return sum_
  
  return sumNums(n-1, sum_+n)

if __name__ == "__main__":
  sumNums(2, 0)