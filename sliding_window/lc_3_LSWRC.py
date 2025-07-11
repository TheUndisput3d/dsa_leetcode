# Longest Substring Without Repeating Characters

from typing import List

## Brute Force Approach
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        for i in range(len(s)):
            subs = ""
            for j in range(i, len(s)):
                curr = s[j]
                if curr in subs:
                    break
                subs += s[j]
                ans = max(ans, j-i+1)
        return ans
    

## Optimal Approach
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i, j = 0, 1
        ans = ""
        count = 0
        while i < len(s):
            
