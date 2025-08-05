from typing import List

## Brute Force Approach
# T.C: O(n^2)
# S.C: O(n)
class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        n = len(fruits)
        used_baskets = set()
        placed = 0

        for i in range(n):
            for j in range(n):
                if j in used_baskets:
                    continue
                if baskets[j] >= fruits[i]:
                    used_baskets.add(j)
                    placed += 1
                    break

        return n - placed
    
## Optimal Approach
# T.C: O(n^2)
# S.C: O(1)
class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        
        count = 0
        n = len(baskets)
        for fruit in fruits:
            unset = 1
            for i in range(n):
                if fruit <= baskets[i]:
                    baskets[i] = 0
                    unset = 0
                    break
            count += unset
        return count