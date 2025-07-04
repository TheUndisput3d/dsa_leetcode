from typing import List
class Solution:
    def solve(self, ind, total, subset, target, candidates, result):
        if total == target:
            result.add(tuple(sorted(subset.copy())))
            return 
        elif total > target:
            return
        if ind >= len(candidates):
            return
        
        subset.append(candidates[ind])
        self.solve(ind+1, total+candidates[ind], subset, target, candidates, result)
        subset.pop()
        self.solve(ind+1, total, subset, target, candidates, result)
        
        return [list(i) for i in result]
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # candidates.sort()
        print(self.solve(0, 0, [], target, candidates, set()))
        
    

obj = Solution()
print(obj.combinationSum([2,5,2,1,2], 5))
