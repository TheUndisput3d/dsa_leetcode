# T.C: O(n^2)
# S.C: O(1)
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)
        for i in range(1, n // 2 + 1):
            if n % i == 0 and s[:i] * (n // i) == s:
                return True
        
        return False
    
# T.C: O(n)
# S.C: O(n)
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        return s in (s+s)[1:-1]