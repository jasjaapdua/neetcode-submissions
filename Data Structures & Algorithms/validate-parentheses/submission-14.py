class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        close_braces = {
            ")":"(",
            "}":"{",
            "]":"["
        }

        for b in s:
            if b in "([{":
                stack.append(b)
            else:
                if not stack or stack[-1] != close_braces[b]:
                    return False
                stack.pop()
        
        if not stack:
            return True
        
        return False