from typing import List

# T.C : O(n+p), p = total number of conflicting points, n = total points
# S.C : O(n)
class Solution:
    def maxSubarrays(self, n: int, conflictingPairs: List[List[int]]) -> int:
        valid = 0

        conflictingPoints = [[] for i in range(n+1)]

        for p in conflictingPairs:
            a = min(p[0], p[1])
            b = max(p[0], p[1])

            conflictingPoints[b].append(a)
        
        maxConflict = 0
        secondMaxConflict = 0

        extra = [0] * (n+1)
        # extra[i] = no. of extra subarrays by removing the conflicting point i

        for end in range(1, n+1): # visiting each point and treating them as subarray ending at this point
            for u in conflictingPoints[end]:
                if u >= maxConflict:
                    secondMaxConflict = maxConflict
                    maxConflict = u
                elif u > secondMaxConflict:
                    secondMaxConflict = u

            valid += end - maxConflict
            extra[maxConflict] += maxConflict - secondMaxConflict
        
        return valid + max(extra)
                
