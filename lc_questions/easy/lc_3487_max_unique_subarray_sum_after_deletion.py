from typing import List

#T.C: O(n)
#S.C: O(n)
class Solution:
    def maxSum(self, nums: List[int]) -> int:
        positiveNumSet = set()

        for num in nums:
            if num > 0:
                positiveNumSet.add(num)
        
        if len(positiveNumSet) == 0:
            return max(nums)
        
        return sum(positiveNumSet)


class Solution:
    def maxSum(self, nums: List[int]) -> int:
        
        positiveNumsSet = set([num for num in nums if num > 0])

        return max(nums) if len(positiveNumsSet) == 0 else sum(positiveNumsSet)
    

class Solution:
    def maxSum(self, nums: List[int]) -> int:
        if all(n<0 for n in nums):
            return max(nums)
        
        unique = set(nums)

        return sum(n for n in unique if n > 0)

        
# T.C: O(n)
# S.C: O(1) #due to fixed size array
class Solution:
    def maxSum(self, nums: List[int]) -> int:
        max_value = max(nums)

        if all(n < 0 for n in nums):
            return max_value
        
        seen = [False] * 101

        for n in nums:
            if 0 <= n <= 100:
                seen[n] = True
        
        return sum(i for i in range(1, 101) if seen[i])




