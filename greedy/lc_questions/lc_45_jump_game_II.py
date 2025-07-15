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
