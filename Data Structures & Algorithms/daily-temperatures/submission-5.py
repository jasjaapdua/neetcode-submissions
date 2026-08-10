class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []
        
        i = 0
        while i < len(temperatures):
            current = temperatures[i]
            if i == 0:
                stack.append(i)
            else:
                while stack and current > temperatures[stack[-1]]:
                    result[stack[-1]] = i - stack[-1]
                    stack.pop()
                stack.append(i)
            i += 1
        return result