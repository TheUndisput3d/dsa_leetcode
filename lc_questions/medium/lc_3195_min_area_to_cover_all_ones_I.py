class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        r, c = len(grid), len(grid[0])
        minRow = r
        maxRow = -1
        minCol = c
        maxCol = -1

        for i in range(r):
            for j in range(c):
                if grid[i][j] == 1:
                    minRow = min(minRow, i)
                    maxRow = max(maxRow, i)
                    minCol = min(minCol, j)
                    maxCol = max(maxCol, j)
        
        return (maxRow - minRow + 1) * (maxCol - minCol + 1)