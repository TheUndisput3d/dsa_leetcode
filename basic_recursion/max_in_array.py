## calculating max number using recursion

def calcMax(arr, max_, i):
  if i == -1:
    return max_
  
  return calcMax(arr, max(max_, arr[i]), i-1)

if __name__ == "__main__":
  calcMax([5, 4, 2, 1], -92838, 4-1)

