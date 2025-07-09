# steps
    # Reverse the infix
    # Infix to Postfix
    # Reverse the answer

class Solution:
    def precedence(self, ch):
        if ch == "^":
            return 5
        elif ch == "*" or ch == "/":
            return 3
        elif ch == "+" or ch == "-":
            return 2
        else:
            return 1
            
    def InfixtoPrefix(self, s):
        s = s[::-1]
        s = (
            s
            .replace("(", "temp")
            .replace(")", "(")
            .replace("temp", ")")
        )
        stack = []
        result = []
    
        for c in s:
            if ("a" <= c <= "z") or ("A" <= c <= "Z") or ("0" <= c <= "9"):
                result.append(c)
            elif c == "(":
                stack.append(c)
            elif c == ")":
                while stack and stack[-1] != "(":
                    result.append(stack.pop())
                stack.pop()
            else:
                while stack and self.precedence(c) <= self.precedence(stack[-1]):
                    result.append(stack.pop())
                stack.append(c)
    
        while stack:
            result.append(stack.pop())
    
        return "".join(result)[::-1]
