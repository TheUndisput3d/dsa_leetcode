from typing import List

class Solution:
   def nextGreaterElements(self, nums: List[int]) -> List[int]:
       n = len(nums)
       result = [-1] * n  # Initialize result array with -1
       stack = []  # Stack to store potential next greater elements

       # Process array indices from 2n-1 down to 0 (simulating circular array)
       for i in range(2 * n - 1, -1, -1):
           # Remove elements from stack that are smaller than or equal to current element
           while stack and stack[-1] <= nums[i % n]:
               stack.pop()

           # Update result only for the first n indices (original array)
           if i < n:
               if stack:  # If stack is not empty
                   result[i] = stack[-1]
                   
           # Add current element to stack
           stack.append(nums[i % n])
           
       return result