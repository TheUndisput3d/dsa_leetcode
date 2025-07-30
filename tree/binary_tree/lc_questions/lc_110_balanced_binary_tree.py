from typing import List, Optional

## T.C: O(N)
## S.C: O(H)
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def solve(node):
            if node == None:
                return 0
            
            left = solve(node.left)
            if left == -1:
                return -1
            right = solve(node.right)
            if right == -1:
                return -1
            
            if abs(left - right) > 1:
                return -1

            return 1 + max(left, right)

        x = solve(root)

        return x != -1
            
