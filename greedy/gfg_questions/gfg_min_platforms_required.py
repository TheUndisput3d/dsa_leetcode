## Brute-Force Approach: using 2 nested loops
## T.C: O(n^2)
## S.C: O(1)
def minPlatform(arr, dep):
    n = len(arr)
    res = 0

    # Run a nested for-loop to find the overlap
    for i in range(n):

        # Initially one platform is needed
        cnt = 1
        for j in range(n):
            if i != j:

                # Increment cnt if trains have overlapping
                # time.
                if arr[i] >= arr[j] and dep[j] >= arr[i]:
                    cnt += 1

        # Update the result
        res = max(cnt, res)
    return res


## Optimal-Approach: using sorting and two pointers
# T.C: O(nlogn)
# S.C: O(1)
def minPlatform(arr, dep):
    n = len(arr)
    res = 0

    # Sort the arrays
    arr.sort()
    dep.sort()
    
    # Pointer to track the departure times
    j = 0

    # Tracks the number of platforms needed at any given time
    cnt = 0
    
    # Check for each train
    for i in range(n):
        
        # Decrement count if other 
        # trains have left 
        while j < n and dep[j] < arr[i]:
            cnt -= 1
            j += 1
        
        # one platform for current train 
        cnt += 1
        
        res = max(res, cnt)
    
    return res
