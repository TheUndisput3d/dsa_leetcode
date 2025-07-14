from typing import List

## T.C: O(n)
## S.C: O(1)
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        maxIndex = 0

        for i in range(n):
            if i > maxIndex:
                return False
            
            nextIndex = i + nums[i]
            maxIndex = max(maxIndex,nextIndex)
            if maxIndex == n-1:
                break

        return True