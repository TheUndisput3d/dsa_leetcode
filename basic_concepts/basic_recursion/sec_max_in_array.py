def calcSecMax(arr, prev_max, max_, i):
  if i == -1:
    return prev_max
  
  return calcSecMax(arr, max_, max(max_, arr[i]), i-1)

if __name__ == "__main__":
  calcSecMax([52, 4, 2, 19], -92838, -234325, 3)