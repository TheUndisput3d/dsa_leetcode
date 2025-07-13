from typing import List

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        return self.solve(1, 0, [], n, k)

    def solve(self, last, total, subset, n, k):
        if total == n and len(subset) == k:
            return [subset.copy()]
        if total > n or len(subset) > k:
            return []
        ans = []
        for i in range(last, 10):
            subset.append(i)
            ans.extend(self.solve(i+1, total+i, subset, n, k))
            subset.pop()
        return ans