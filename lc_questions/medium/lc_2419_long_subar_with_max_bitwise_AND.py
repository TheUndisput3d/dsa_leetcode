from typing import List

# T.C: O(n)
# S.C: O(1)
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        maxVal = 0
        streak = 0
        result = 0

        for num in nums:
            if num > maxVal:
                maxVal = num
                result = 0
                streak = 0
            if num == maxVal:
                streak += 1
            else:
                streak = 0
            
            result = max(result, streak)
        return result
