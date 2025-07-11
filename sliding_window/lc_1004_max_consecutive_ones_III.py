from typing import List

## Brute-Force Approach: Generating all the substrings
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        """
        This method finds the maximum number of consecutive 1s in a binary array,
        allowing at most 'k' flips of 0s to 1s.

        Time Complexity: O(n²)
        - Two nested loops; worst case checks every pair (i, j)

        Space Complexity: O(1)
        - No additional space used that scales with input size
        """

        max_len = 0         # Tracks the maximum length found
        n = len(nums)       # Length of input array

        # Outer loop: start index of the window
        for i in range(n):
            zeros = 0       # Reset count of flipped zeros for each starting index

            # Inner loop: end index of the window
            for j in range(i, n):
                curr = nums[j]

                # If current value is 0, increase zero count
                if not curr:
                    zeros += 1

                # If number of flipped zeros exceeds k, stop expanding window
                if zeros > k:
                    break

                # Update max_len if this window is longer than previous best
                max_len = max(max_len, j - i + 1)

        # Return the length of the longest valid window
        return max_len
    
## Better Approach
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        """
        Finds the longest subarray containing only 1s after flipping at most k zeroes.

        Time Complexity: O(n)
        - Each element is visited at most twice: once by j and possibly once by i.
        - The sliding window ensures linear traversal.

        Space Complexity: O(1)
        - Only uses a few integer variables; no extra space that grows with input size.
        """

        max_len = 0      # Stores the maximum length of valid subarray
        n = len(nums)    # Length of the input array

        i, j = 0, 0      # Sliding window pointers: i (start), j (end)
        zeros = 0        # Number of zeroes in the current window

        # Expand the window by moving j forward
        while j < n:
            curr = nums[j]

            if not curr:
                zeros += 1  # Count 0s that we may flip

            # If number of zeros exceeds k, shrink window from the left
            while zeros > k:
                if nums[i] == 0:
                    zeros -= 1  # Adjust count when removing a zero
                    i += 1          # Move start of window forward

            # Update max_len with the current window size
            max_len = max(max_len, j - i + 1)
            j += 1  # Move end of window forward

        return max_len  # Final answer: longest valid window size
    
## Optimal Approach
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        """
        Finds the length of the longest contiguous subarray that contains only 1s,
        allowing at most 'k' flips of 0s to 1s.

        Time Complexity: O(n)
        - Each element is visited at most twice (once by j, possibly once by i).
        - Efficient one-pass sliding window solution.

        Space Complexity: O(1)
        - No extra data structures used beyond a few variables.
        """

        max_len = 0          # Tracks the maximum length found so far
        n = len(nums)        # Total length of the input array

        i, j = 0, 0          # Two pointers defining the window: i (left), j (right)
        zeros = 0            # Number of zeroes within the window (flipped if ≤ k)

        # Traverse the array with right pointer j
        while j < n:
            curr = nums[j]

            # If current element is 0, count it toward our flips
            if not curr:
                zeros += 1

            # If we've exceeded the allowed flips, shrink window from the left
            if zeros > k:
                if nums[i] == 0:
                    zeros -= 1  # Remove the impact of the left-most flipped zero
                i += 1          # Move left boundary forward

            # If current window is valid, update maximum length
            if zeros <= k:
                max_len = max(max_len, j - i + 1)

            j += 1  # Expand window by moving right pointer forward

        # Return the length of the longest valid window
        return max_len