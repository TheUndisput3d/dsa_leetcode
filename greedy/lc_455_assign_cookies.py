from typing import List

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        """
        Time Complexity: O(n log n + m log m)
        - Sorting g and s takes O(n log n) and O(m log m)
        - Single linear scan through both lists after sorting → O(n + m)

        Space Complexity: O(1)
        - Sorting is in-place and only constant extra space is used
        """

        g.sort()
        s.sort()
        
        cookieIndex = 0
        contentChildren = 0

        # Try to satisfy each child with the smallest cookie that fits
        while cookieIndex < len(s) and contentChildren < len(g):
            if s[cookieIndex] >= g[contentChildren]:
                contentChildren += 1
            cookieIndex += 1

        return contentChildren
