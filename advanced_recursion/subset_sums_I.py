class Solution:
    def solve(self, nums, index, subset, result):
        # Base case: if index reaches the length of the array,
        # add the sum of the current subset to the result.
        if index >= len(nums):
            result.append(sum(subset))
            return
        
        # Choice 1: Include the current element in the subset.
        subset.append(nums[index])
        self.solve(nums, index + 1, subset, result)
        
        # Backtrack: Remove the last element to explore the exclusion branch.
        subset.pop()
        
        # Choice 2: Exclude the current element and move to the next.
        self.solve(nums, index + 1, subset, result)

    def subsetSums(self, arr):
        result = []
        self.solve(arr, 0, [], result)
        return result