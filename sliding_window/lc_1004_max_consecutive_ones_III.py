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
    
## Optimal Approach-I
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
    
## Optimal Approach-II
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        """
        Finds the longest contiguous subarray of 1s allowing at most 'k' flips from 0 to 1.

        Time Complexity: O(n)
        - Each element is visited at most twice: once by r (right pointer) and once by l (left pointer).
        - The window expands and contracts dynamically, maintaining linear performance.

        Space Complexity: O(1)
        - Only uses a few integer variables (no data structures scaling with input size).
        """

        l = r = 0           # l = start of window, r = end of window
        max_len = 0         # Stores the maximum length found
        num_zeros = 0       # Count of zeroes within the window that we've "flipped"
        n = len(nums)       # Length of input array

        # Slide the window using the right pointer
        while r < n:
            if nums[r] == 0:
                num_zeros += 1  # Count the number of zeros as potential flips

            # If the number of zeros exceeds k, shrink the window from the left
            if num_zeros > k:
                if nums[l] == 0:
                    num_zeros -= 1  # Undo a flip if we shrink past a zero
                l += 1  # Move left pointer forward

            # Calculate window length and update maximum if needed
            len_ = r - l + 1
            max_len = max(max_len, len_)

            # Move right pointer forward to expand the window
            r += 1

        return max_len  # Final result: the longest subarray that satisfies the condition