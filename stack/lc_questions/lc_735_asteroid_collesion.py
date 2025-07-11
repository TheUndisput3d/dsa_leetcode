from typing import List

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for i in range(len(asteroids)):
            curr = asteroids[i]
            if curr > 0:
                stack.append(curr)
            else:
                while stack and stack[-1] > 0 and abs(curr) > stack[-1]:
                    stack.pop()

                if stack and abs(curr) == stack[-1]:
                    stack.pop()

                elif not stack or stack[-1] < 0:
                    stack.append(curr)   

        return stack
                 
