from typing import List

## T.C: O(n * 32) ~ O(n)
## S.C: O(n)

class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        prev = set()
        curr = set()
        result = set()

        for num in arr:
            for x in prev:
                curr.add(num | x)
                result.add(num | x)
            
            curr.add(num)
            result.add(num)
            prev = curr.copy()
            curr.clear()
        
        return len(result)
