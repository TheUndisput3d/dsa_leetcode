from collections import deque
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

### DFS Solution
# T.C: O(N), where N -> No. of nodes
# S.C: O(H), where H is the (no of nodes along the longest path to the bottom)
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.solve(root)
    
    def solve(self, node):
        if node == None:
            return 0

        one = self.solve(node.left)
        two = self.solve(node.right)
        
        return 1 + max(one, two)


### BFS Solution
# T.C: O(N), where N -> No. of nodes
# S.C: O(N)
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        
        queue = deque([])
        queue.append(root)
        height = 0

        while len(queue) != 0:
            level_size = len(queue)
            height += 1
            for _ in range(level_size):
                curr = queue.popleft()

                if curr.left is not None:
                    queue.append(curr.left)

                if curr.right is not None:
                    queue.append(curr.right)
        
        return height
    

