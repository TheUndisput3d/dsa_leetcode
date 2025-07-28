from typing import List

# T.C: O(n)
class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        n = len(nums)

        i, j = 0, 1
        count = 0

        while j+1 < n:
            if (nums[i] < nums[j] > nums[j+1]) or (nums[i] > nums[j] < nums[j+1]):
                i = j
                count += 1
            
            j += 1

        return count

        