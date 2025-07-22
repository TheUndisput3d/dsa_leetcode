## calculating max number using recursion
def calcMax(arr, max_, i):
  if i == -1:
    return max_
  
  return calcMax(arr, max(max_, arr[i]), i-1)


def calcMin(arr, min_, i):
  if i == -1:
    return min_

  return calcMin(arr, min(min_, arr[i]), i-1)

if __name__ == "__main__":
  calcMax([5, 4, 2, 1], -92838, 4-1)
  calcMin([234, -345321, -1, -445], 9384523, 3)

