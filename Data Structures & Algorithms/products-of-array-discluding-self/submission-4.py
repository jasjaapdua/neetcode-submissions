class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        size = len(nums)
        product_left = [1] * size
        product_right = [1] * size

        i = 1
        while i < size:
            product_left[i] = product_left[i-1] * nums[i-1]
            i += 1
        
        i = size - 2
        while i >= 0:
            product_right[i] = product_right[i+1] * nums[i+1]
            i -= 1
        
        result = []
        for a, b in zip(product_left, product_right):
            result.append(a * b)
        
        return result