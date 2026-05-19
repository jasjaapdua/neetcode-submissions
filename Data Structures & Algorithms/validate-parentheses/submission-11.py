class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        def close_brace(p):
            brace_map = {
                ']': '[',
                ')': '(',
                '}': '{'
            }
            return brace_map[p]

        for p in s:
            if p in '({[':
                stack.append(p)
            else:
                if len(stack) > 0 and stack[-1] == close_brace(p):
                    stack.pop()
                else:
                    return False

        return len(stack) == 0

        