class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights) - 1
        result = 0

        while left <= right:
            current = min(heights[left], heights[right]) * (right - left)
            result = max(result, current)

            if heights[left] < heights[right]:
                left += 1
            
            elif heights[right] < heights[left]:
                right -= 1
            
            else:
                left += 1
            
        return result