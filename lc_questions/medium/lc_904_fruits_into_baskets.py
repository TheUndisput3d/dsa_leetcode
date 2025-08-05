from typing import List

## T.C: O(N)
## O.C: O(N)
class Solution:
    def totalFruit(self, fruits: List[int]) -> int: 
        n = len(fruits)

        map_ = {}

        i = j = 0
        count = 0

        while j < n:
            map_[fruits[j]] = map_.get(fruits[j], 0) + 1

            if len(map_) <= 2:
                count = max(count, j-i+1)
            else:
                map_[fruits[i]] -= 1
                if map_[fruits[i]] == 0:
                    del map_[fruits[i]]
                i += 1
            
            j += 1

        return count
