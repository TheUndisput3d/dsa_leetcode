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
    

###################################################---Using Set for Brute Force Approach---##############################################
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        for i in range(len(s)):
            set_ = set()
            for j in range(i, len(s)):
                if s[j] in set_:
                    break
                set_.add(s[j])
                max_len = max(max_len, j-i+1)
        return max_len
    

########################################################---Using list as hash to store the last occurence of strings using Ascii---####################
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
            
#####################################---Using dict to store the last occurences of chars---#################################
## Optimal Approach
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #################################### Using Dict ##################################
        
        # Time Complexity: O(n)
        # - Each character is processed at most twice: once by j and maybe by i.
        # - Dictionary lookups and updates are O(1) on average.

        # Space Complexity: O(m)
        # - m is the size of the character set used (e.g., 26 for lowercase letters, 128 for ASCII).
        # - Dictionary stores character positions, so space grows with unique characters.

        n = len(s)              # Total length of input string
        max_len = 0             # Tracks the length of the longest valid substring
        i, j = 0, 0             # Two pointers for sliding window: i (start), j (end)
        my_dict = {}            # Dictionary to store the last index of each character

        # Iterate through the string using j as the end of the window
        while j < n:
            curr = s[j]         # Current character at position j

            # If current character is already seen and within current window
            if curr in my_dict:
                if my_dict[curr] >= i:
                    # Move the start pointer i just past the last occurrence of current character
                    i = my_dict[curr] + 1

            # Calculate the current window length
            curr_len = j - i + 1

            # Update maximum length if this window is longer
            max_len = max(max_len, curr_len)

            # Store/update the index of the current character
            my_dict[curr] = j

            # Expand the window by moving j forward
            j += 1

        # Return the length of the longest substring without repeating characters
        return max_len

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ####################################- Using Dict -##################################
        n = len(s)
        max_len = 0
        i, j = 0, 0
        my_dict = {}
        
        while j < n:
            curr = s[j]
            if curr in my_dict:
                left = max(left, my_dict[curr]+1)
            curr_len = j - i + 1
            max_len = max(max_len, curr_len)
            my_dict[curr] = j
            j += 1
        
        return max_len


        
        


        



        


        

