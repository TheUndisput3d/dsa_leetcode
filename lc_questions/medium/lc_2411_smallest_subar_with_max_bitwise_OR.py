from typing import List

# T.C: O(n) [the inner for loop runs constant no. of times (32)]
# S.C: O(1) [setBitIndex is constant space of size 32 and not considering result which is returned]
class Solution:
    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        n = len(nums)
        setBitIndex = [-1] * 32
        result = [1] * len(nums)

        for i in range(n-1, -1, -1):
            endIndex = i
            for j in range(0, 32):
                if not (nums[i] & (1 << j)):
                    endIndex = max(endIndex, setBitIndex[j])
                else:
                    setBitIndex[j] = i
            
            result[i] = endIndex - i + 1

        return result