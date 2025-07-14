## T.C: O(nlogn) + O(n) ~ O(nlogn)
## S.C: O(n)
def fractionalKnapsack(val, weight, capacity):
  arr = [(v, w) for v, w in zip(val, weight)]

  arr.sort(key=lambda x: x[0]/x[1], reverse=True)
  ans = 0

  for i in range(len(arr)):
    curr = arr[i]

    if capacity - curr[1] >= 0:
      ans += curr[0]
      capacity -= curr[1]
    else:
      ans += curr[0]/curr[1] * capacity
      break

  return ans

## T.C: O(nlogn) + O(n) 
## S.C: O(1)
def fractionalKnapsack(arr, capacity):
  arr.sort(key=lambda x: x[0]/x[1], reverse=True)
  ans = 0
  notTaken = set()

  for i in range(len(arr)):
    curr = arr[i]

    if capacity - curr[1] >= 0:
      ans += curr[0]
      capacity -= curr[1]
    else:
      notTaken.add(i)

  if capacity:
    for i in notTaken:
      rem = arr[i]
      ans += rem[0]/rem[1] * capacity
      break
  return ans




if __name__ == "__main__":
    val = [60, 100, 200, 100]
    wt = [10, 20, 50, 50]
    capacity = 40

    print(fractionalKnapsack(val, wt, capacity))    

