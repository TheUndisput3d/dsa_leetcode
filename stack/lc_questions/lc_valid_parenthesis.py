## Leetcode: Valid Prenthesis

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, val):
        self.stack.append(val)

    def pop(self):
        return self.stack.pop()

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)

class Solution:
    def isValid(self, s: str) -> bool:
        st = Stack()
        hash_ = {"}": "{", ")": "(", "]": "["}

        for c in s:
            if c not in hash_:
                st.push(c)
            else:
                if st.is_empty():
                    return False
                ch = st.pop()
                if ch != hash_[c]:
                    return False
        
        return True if st.is_empty() else False