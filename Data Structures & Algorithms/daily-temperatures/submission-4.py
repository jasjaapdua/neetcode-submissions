class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []

        for i, temp in enumerate(temperatures):
            if i == 0:
                stack.append(i)
            else:
                while(stack and temp > temperatures[stack[-1]]):
                    result[stack[-1]] = i - stack[-1]
                    stack.pop()
                stack.append(i)
        return result

