
## Extreme Brute-Force (Recursion)
# Generating all the possible combinations
# T.C: O(2^N)
# S.C: O(N)
class Solution: 
    def __init__(self):
        self.size = float('inf')
        self.ans = []

    def solve(self, coins, i, v, N):
        if N == 0:
            if len(v) < self.size:
                self.size = len(v)
                self.ans = v.copy()
            return

        if i < 0 or N < 0:
            return

        # Exclude the current coin
        self.solve(coins, i - 1, v, N)

        # Include the current coin
        v.append(coins[i])
        self.solve(coins, i, v, N - coins[i])
        v.pop()  # backtrack

    def minPartition(self, N):
        coins = [1, 2, 5, 10, 20, 50, 100, 200, 500, 2000]
        self.size = float('inf')
        self.ans = []
        self.solve(coins, len(coins) - 1, [], N)
        return self.ans
    


### Optimal Approach (Greedy Solution) ---- Best Approach

## T.C: O(N)
## S.C: O(N)
class Solution:
    def minPartition(self, N):
        # code here
        currency = [1, 2, 5, 10, 20, 50, 100, 200, 500, 2000]
        
        ans = []

        for i in range(len(currency)-1, -1, -1):
            curr = currency[i]

            while N >= curr:
                N -= curr
                ans.append(curr)
        
        return ans

## My Solution (Similar to optimal but, Above approach is better)
class Solution:
    def minPartition(self, N):
        currency = [1, 2, 5, 10, 20, 50, 100, 200, 500, 2000]
        ans = 0
        lst = []

        for i in range(len(currency)-1, -1, -1):
            curr = currency[i]
            if curr > N:
                continue
            
            ### This is a little inefficient
            # while ans < N:      ### This works too
            #     if ans+curr > N:
            #         break
            #     ans += curr
            #     lst.append(curr)
            
            # Greedy Optimization to above while loop.
            count = N // curr ### More optimized than above while loop
            lst.extend([curr] * count)
            N -= count * curr
                        
            if ans == N:
                return lst


