class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        ops = {
            '+': lambda a, b : a + b,
            '-': lambda a, b : a - b,
            '*': lambda a, b : a * b,
            '/': lambda a, b : a / b,
        }

        for t in tokens:
            try:
                number = int(t)
                stack.append(number)
            except ValueError:
                b = stack.pop()
                a = stack.pop()
                result = ops[t](a, b)
                stack.append(int(result))
        return stack[0]
        