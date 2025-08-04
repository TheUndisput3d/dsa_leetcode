from typing import List

## T.C: O(nlogn)
## S.C: O(n)
class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        from collections import Counter

        mp = {}
        minEl = float('inf')

        for num in basket1:
            minEl = min(minEl, num)
            mp[num] = mp.get(num, 0) + 1
        
        for num in basket2:
            minEl = min(minEl, num)
            mp[num] = mp.get(num, 0) - 1

        finalList = []
        for cost, count in mp.items():
            if count == 0:
                continue
            
            if abs(count) % 2 != 0:
                return -1  # can't make them equal if counts differ by odd
            
            for _ in range(abs(count) // 2):
                finalList.append(cost)

        finalList.sort()

        result = 0
        n = len(finalList)
        for i in range(n // 2):
            # Either pay the cost of using finalList[i] or a double swap via minEl
            result += min(finalList[i], 2 * minEl)

        return result