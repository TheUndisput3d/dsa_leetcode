# Longest Substring Without Repeating Characters

from typing import List

## Brute Force Approach
# T.C: O(n^2)
# S.C: O(n)
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0  # Variable to store the length of the longest valid substring

        for i in range(len(s)):  # Outer loop picks each starting index
            subs = ""  # Temporary substring to hold non-repeating characters

            for j in range(i, len(s)):  # Inner loop extends the substring
                curr = s[j]  # Current character

                if curr in subs:  # Check for duplicate character
                    break  # Stop this substring search

                subs += s[j]  # Append current character to substring

                ans = max(ans, j - i + 1)  # Update max length if needed

        return ans  # Return the longest length found
    

## Optimal Approach
# T.C: O(n)
# S.C: O(1)
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Variable to keep track of the maximum length of substring without repeating characters
        max_len = 0

        # Two pointers for sliding window
        i, j = 0, 0

        # Array to store the last seen index of each character using ASCII values
        hash_ = [-1] * 255  # Assumes extended ASCII (up to 255)

        # Traverse the string using the 'j' pointer
        while j < len(s):
            currCharAsc = ord(s[j])  # Convert current character to its ASCII value

            # If the current character was seen before and lies within the current window
            if hash_[currCharAsc] != -1:
                if hash_[currCharAsc] >= i:
                    # Move the start of the window 'i' to exclude the repeated character
                    i = hash_[currCharAsc] + 1

            # Calculate the length of the current window and update max_len if it's larger
            subsLen = j - i + 1
            max_len = max(max_len, subsLen)

            # Update the last seen index of the current character
            hash_[currCharAsc] = j

            # Move the end of the window forward
            j += 1

        # Return the maximum length found
        return max_len
            
