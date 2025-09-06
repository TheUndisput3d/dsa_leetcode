# T.C: O(n)
# S.C: O(1)

from typing import List
class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        maxDiag = float('-inf')
        maxArea = float('-inf')
        for dim in dimensions:
            l = dim[0]
            w = dim[1]
            diag_l = l*l + w*w
            area = l * w
            if diag_l > maxDiag:
                maxDiag = diag_l
                maxArea = area
            elif diag_l == maxDiag:
                maxArea = max(maxArea, area)
        return maxArea