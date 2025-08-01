from typing import List

## T.C: O(numRows * numRows) -> O(n^2)
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = []
        for i in range(numRows):
            result.append([1] * (i + 1))

            for j in range(1, i):
                result[i][j] = result[i-1][j] + result[i-1][j-1]
        
        return result