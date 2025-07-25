class Solution:
  def strStr(self, haystack: str, needle: str) -> int:
      n = len(haystack)
      i, j = 0, len(needle)-1

      while j < n:
          if haystack[i:j+1] == needle:
              return i
          
          i += 1
          j += 1
          
      return -1
    
# T.C: O(n * m)
# S.C: O(1)
class Solution:
  def strStr(self, haystack: str, needle: str) -> int:
      n = len(haystack)
      m = len(needle)

      for i in range(n-m+1):
          if haystack[i:i+m] == needle:
              return i

      return -1


# this can give TLE but the logic is same as above
class Solution:
  def strStr(self, haystack: str, needle: str) -> int:
      n = len(haystack)
      m = len(needle)

      for i in range(n-m+1):
        for j in range(m):
          if haystack[i+j] != needle[j]:
            break
          if j == len(needle) - 1:
              return True
    
      return -1
        