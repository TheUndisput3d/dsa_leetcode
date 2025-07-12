from typing import List

## Optimal Approach
class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        """
        Time Complexity: O(2k)
        - We compute sum of first k elements (O(k))
        - Then run a loop of size k to try different left-right combinations (O(k))

        Space Complexity: O(1)
        - Only a few integer variables are used
        """

        n = len(cardPoints)
        lsum = rsum = 0

        # Take first k cards from the left
        for i in range(k):
            lsum += cardPoints[i]
            
        max_sum = lsum

        rIndex = n - 1

        # Try shifting cards from right one by one
        for i in range(k - 1, -1, -1):
            lsum -= cardPoints[i]
            rsum += cardPoints[rIndex]
            max_sum = max(max_sum, lsum + rsum)
            rIndex -= 1

        return max_sum
    
## Optimal Approach
class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:

        n = len(cardPoints)
        lsum = rsum = 0
        
        for i in range(n-1, n-k-1, -1):
            rsum += cardPoints[i]
        
        max_sum = rsum

        lIndex = 0
        for i in range(n-k, n):
            rsum -= cardPoints[i]
            lsum += cardPoints[lIndex]
            max_sum = max(max_sum, lsum+rsum)
            lIndex += 1
        
        return max_sum

