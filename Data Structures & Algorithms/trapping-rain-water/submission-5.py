class Solution:
    def trap(self, height: List[int]) -> int:
        max_right = [0] * len(height)
        max_left = [0] * len(height)
        result = [0] * len(height)

        i = 1
        while i < len(height):
            max_left[i] = max(max_left[i - 1], height[i - 1])
            i += 1
        
        i = len(height) - 2
        while i > 0:
            max_right[i] = max(max_right[i + 1], height[i + 1])
            i -= 1
        

        i = 0
        while i < len(height):
            result[i] = min(max_right[i], max_left[i]) - height[i]
            i += 1

        return sum(vol for vol in result if vol > 0)