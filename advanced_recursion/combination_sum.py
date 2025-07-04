from typing import List
class Solution:
    def solve(self, ind, total, subset, target, candidates, result):
        if total == target:
            result.append(subset.copy())
            return 
        elif total > target:
            return
        if ind >= len(candidates):
            return
        
        subset.append(candidates[ind])
        self.solve(ind, total+candidates[ind], subset, target, candidates, result)
        subset.pop()
        self.solve(ind+1, total, subset, target, candidates, result)
        return result

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        return self.solve(0, 0, [], target, candidates, [])
