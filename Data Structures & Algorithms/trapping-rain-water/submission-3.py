class Solution:
    def trap(self, height: List[int]) -> int:
        size = len(height)
        tallest_left = [0] * size
        tallest_right = [0] * size

        for i in range(1, size):
            tallest_left[i] = max(tallest_left[i - 1], height[i-1])
        
        for i in range(size - 2, -1, -1):
            tallest_right[i] = max(tallest_right[i+1], height[i+1])


        print(tallest_left, tallest_right)
        max_water_column = [
            max(min(tallest_left[i], tallest_right[i]) - h, 0)
            for i, h in enumerate(height)
        ]

        return sum(max_water_column)