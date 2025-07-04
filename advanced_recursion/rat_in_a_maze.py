from typing import List

def findPathHelper(
        i: int,
        j: int, 
        matrix: List[List[int]],
        n: int,
        ans: List[str],
        vis: List[List[int]],
        move: str
):
    if i == n-1 and j == n-1:
        ans.append(move)
        return
    
    # downward
    if i+1 < n and not vis[i+1][j] and matrix[i+1][j]:
        vis[i][j] = 1
        findPathHelper(i+1, j, matrix, n, ans, vis, move+"D")
        vis[i][j] = 0

    # upward
    if i-1 >= 0 and not vis[i-1][j] and matrix[i-1][j]:
        vis[i][j] = 1
        findPathHelper(i-1, j, matrix, n, ans, vis, move+"U")
        vis[i][j] = 0

    # leftward
    if j-1 >= 0 and not vis[i][j-1] and matrix[i][j-1]:
        vis[i][j] = 1
        findPathHelper(i, j-1, matrix, n, ans, vis, move+"L")
        vis[i][j] = 0

    # rightward
    if j+1 < n and not vis[i][j+1] and matrix[i][j+1]:
        vis[i][j] = 1
        findPathHelper(i, j+1, matrix, n, ans, vis, move+"R")
        vis[i][j] = 0

def ratMaze(matrix: List[List[int]]) -> List[str]:
    n = len(matrix)
    ans = []
    vis = [[0 for _ in range(n)] for _ in range(n)]

    if matrix[0][0]:
        findPathHelper(0, 0, matrix, n, ans, vis, "")

    return ans

if __name__ == "__main__":
    matrix = [[1, 0, 0, 0], [1, 1, 0, 0], [1, 1, 0, 0], [0, 1, 1, 1]]
    i = 0
    for path in ratMaze(matrix):
        i += 1
        print(f"Path-{i}: {path}")

