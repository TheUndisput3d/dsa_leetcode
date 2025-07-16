## Brute Force Approach: Recursion
# T.C: O(n!)
# S.C: O(n)
class Solution:
    def jump(self, nums: List[int]) -> int:
        def solve(index, jump):

            if index >= len(nums)-1:
                return jump
            
            min_jump = float('inf')

            for i in range(1, nums[index]+1):
                min_jump = min(min_jump, solve(index+i, jump+1))

            return min_jump

        solve(0, 0)
        return solve(0, 0)


## Recursion (DP - Memoization)
# T.C: O(n^2)
# S.C: O(n)
class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [-1] * n  # dp[i] = min jumps needed to reach the end from index i

        def solve(index):
            if index >= n - 1:
                return 0  # no more jumps needed

            if dp[index] != -1:
                return dp[index]

            min_jumps = float('inf')
            for i in range(1, nums[index] + 1):
                if index + i < n:
                    min_jumps = min(min_jumps, 1 + solve(index + i))

            dp[index] = min_jumps
            return dp[index]

        return solve(0)


## Optimal Approach
# T.C: O(n)
# S.C: O(1)
class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)

        i = j = 0
        farthest = 0
        jump = 0

        while j < n - 1:
            for k in range(i, j+1):
                farthest = max(farthest, k+nums[k])
            i = j + 1
            j = farthest
            jump += 1
            
        return jump


