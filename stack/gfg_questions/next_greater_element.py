
## Optimal Approach
class Solution:
    def nextLargerElement(self, arr):
        ## Optimal Solution: Using Monotonic Stack
        # T.C: O(n)
        # S.C
        stack = []
        ans = [-1] * len(arr)
        for i in range(len(arr)-1, -1, -1):
            while stack and stack[-1] <= arr[i]:
                stack.pop()
            if stack:
                ans[i] = stack[-1]
            stack.append(arr[i])
        return ans
    
####################################################-Brute Force-############################################################################################################

## Brute Force Approach
# T.C: O(n^2)
class Solution:
    def nextLargerElement(self, arr):
        ans = [-1] * len(arr)

        for i in range(len(arr)):
            for j in range(i+1, len(arr)):
                if arr[j] > arr[i]:
                    ans[i] = arr[j]
                    break
        return ans