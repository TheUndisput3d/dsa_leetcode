from typing import Optional

## Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# T.C - O(n)
# S.C - O(n)
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        temp = head
        set_ = set()
        while temp is not None:  
            if temp in set_:        
                return True
            set_.add(temp)
            temp = temp.next
        return False